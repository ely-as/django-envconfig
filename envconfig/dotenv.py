import os
from pathlib import Path

from dotenv import find_dotenv as _find_dotenv


def find_dotenv(
    filename: str = '.env',
    raise_error_if_not_found: bool = False,
    usecwd: bool = False
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
    # and their parent directories
    if not dotenv_path:
        for exec_path in os.get_exec_path():
            path = Path(exec_path)
            while path.as_posix() != '/' and not dotenv_path:
                if (path / filename).is_file():
                    dotenv_path = (path / filename).as_posix()
                path = path.parent
            if dotenv_path:
                break
    if not dotenv_path and raise_error_if_not_found:
        raise IOError('File not found')
    return dotenv_path
