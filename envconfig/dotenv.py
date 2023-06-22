import os
from pathlib import Path
from typing import Optional, Sequence, Union

from dotenv import find_dotenv as _find_dotenv

MAX_DEPTH: int = 10


def find_dotenv(
    filename: str = ".env",
    raise_error_if_not_found: bool = False,
    usecwd: bool = False,
    extra_paths: Optional[Sequence[Union[Path, str]]] = None,
) -> str:
    """Find the path to a relevant dotenv file, or return an empty string.

    Extends :py:func:`dotenv.find_dotenv` by also searching in the execution
    path and their parent directories (e.g. virtualenv directories).
    """
    try:
        dotenv_path = _find_dotenv(filename, raise_error_if_not_found, usecwd)
    except IOError:
        # Reraise this error later if our own search fails
        if raise_error_if_not_found:
            pass
    # If find_dotenv doesn't find a dotenv file, check the execution paths
    # (and extra paths if provided) and their parent directories
    if not dotenv_path:
        paths = [Path(p) for p in extra_paths] if extra_paths else []
        paths += [Path(p) for p in os.get_exec_path()]
        for path in paths:
            i = 0
            while (
                path.resolve() != path.resolve().parent
                and i < MAX_DEPTH
                and not dotenv_path
            ):
                i += 1
                if (path / filename).is_file():
                    dotenv_path = str((path / filename).resolve())
                path = path.parent
            # Return the first dotenv we find
            if dotenv_path:
                break
    if not dotenv_path and raise_error_if_not_found:
        raise IOError("File not found")
    return dotenv_path
