from importlib import import_module
from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_loader
from pathlib import Path
from types import ModuleType
from typing import List, Optional, Union

import django
from django.core.management.utils import get_random_secret_key

# Relative path to settings.py template from django package root dir
RELPATH_TO_SETTINGS_TPL = "conf/project_template/project_name/settings.py-tpl"


def find_project_name(path: Path) -> Optional[str]:
    search = list(
        set(  # noqa: C401
            p.parent.name for p in path.glob("*/[a|w]sgi.py") if p.parent.is_dir()
        )
    )
    return search[0] if len(search) == 1 else None


def get_base_dir(project_name: str) -> Path:
    mod = import_module(project_name)
    return Path(mod.__file__).parent.parent.absolute()  # type: ignore  # noqa


def get_module_settings(project_name: str) -> dict:
    try:
        mod = import_module(f"{project_name}.settings")
        setting_names = [s for s in dir(mod) if s.isupper()]
        return {s: getattr(mod, s) for s in setting_names}
    except ModuleNotFoundError:
        return {}


def get_path_to_settings_template() -> Path:
    return Path(django.__file__).parent / RELPATH_TO_SETTINGS_TPL


def get_template_settings(project_name: str) -> dict:
    template_settings = import_module_from_file(get_path_to_settings_template())
    setting_names = [s for s in dir(template_settings) if s.isupper()]
    settings = {}
    for s in setting_names:
        val = getattr(template_settings, s)
        if isinstance(val, str) and "{{ project_name }}" in val:
            val = val.replace("{{ project_name }}", project_name)
        settings[s] = val
    # Find the correct BASE_DIR
    base_dir = get_base_dir(project_name)
    # Modify the DATABASES setting for correct BASE_DIR
    db_name = settings["DATABASES"]["default"]["NAME"]
    if not isinstance(db_name, Path):
        db_name = Path(db_name)
    db_name = base_dir / db_name.name
    # Overwite some of the defaults
    if isinstance(settings["BASE_DIR"], str):
        settings["BASE_DIR"] = str(base_dir.resolve())
        settings["DATABASES"]["default"]["NAME"] = str(db_name.resolve())
    else:
        settings["BASE_DIR"] = base_dir
        settings["DATABASES"]["default"]["NAME"] = db_name
    settings["DEBUG"] = False  # Ensure DEBUG defaults to False
    settings["SECRET_KEY"] = get_random_secret_key()
    return settings


def import_module_from_file(path: Union[Path, str]) -> ModuleType:
    """Import a Python module based on file path rather than a dotted
    name.
    """
    if isinstance(path, str):
        path = Path(path)
    name = path.name.split(".")[0]
    spec = spec_from_loader(name, SourceFileLoader(name, str(path.resolve())))
    mod = module_from_spec(spec)  # type: ignore  # noqa
    spec.loader.exec_module(mod)  # type: ignore  # noqa
    return mod


def modify_list(list_: List[str], add: List[str], remove: List[str]) -> List[str]:
    """Add and remove items from a list. Preserve order and prevent
    duplication.
    """
    return [a for a in list_ if a not in remove] + [a for a in add if a not in list_]
