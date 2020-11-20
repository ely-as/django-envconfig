from importlib import import_module
from importlib.machinery import SourceFileLoader
from importlib.util import spec_from_loader, module_from_spec
from pathlib import Path
from types import ModuleType
from typing import Union

import django
from django.core.management.utils import get_random_secret_key

# Relative path to settings.py template from django package root dir
RELPATH_TO_SETTINGS_TPL = 'conf/project_template/project_name/settings.py-tpl'

# Settings which are in the settings.py template, but we ignore
TEMPLATE_SETTINGS_IGNORE = (
    'BASE_DIR',   # Will find an incorrect dir, so omit
    'DATABASES',  # Depends on BASE_DIR, see above
    'DEBUG',      # Defaults to True - we force it to False
    'SECRET_KEY'  # Needs to be generated
)


def get_module_settings(project_name: str) -> dict:
    try:
        mod = import_module(f'{project_name}.settings')
        setting_names = [s for s in dir(mod) if s.isupper()]
        return {s: getattr(mod, s) for s in setting_names}
    except ModuleNotFoundError:
        return {}


def get_path_to_settings_template() -> Path:
    return Path(django.__file__).parent / RELPATH_TO_SETTINGS_TPL


def get_template_settings(project_name: str) -> dict:
    template_settings = import_module_from_file(
        get_path_to_settings_template()
    )
    setting_names = [s for s in dir(template_settings) if s.isupper()
                     and s not in TEMPLATE_SETTINGS_IGNORE]
    settings = {}
    for s in setting_names:
        val = getattr(template_settings, s)
        if isinstance(val, str) and '{{ project_name }}' in val:
            val = val.replace('{{ project_name }}', project_name)
        settings[s] = val
    # Set some defaults of our own
    settings['BASE_DIR'] = (
        Path(import_module(project_name).__file__).parent.parent
    )
    settings['DEBUG'] = False  # Ensure DEBUG defaults to False
    settings['SECRET_KEY'] = get_random_secret_key()
    return settings


def import_module_from_file(path: Union[Path, str]) -> ModuleType:
    """Import a Python module based on file path rather than a dotted
    name.
    """
    if isinstance(path, str):
        path = Path(path)
    name = path.name.split('.')[0]
    spec = spec_from_loader(name, SourceFileLoader(name, path.as_posix()))
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore  # noqa
    return mod
