## v0.2.6 (2022-11-09)
### Features
- Added py311 support.

## v0.2.5 (2022-08-14)
### Features
- Added support for Django major version 4.1.

## v0.2.4 (2022-01-08)
### Features
- Added support for Django major version 4.0.

## v0.2.3 (2021-11-04)
### Features
- Added py310 support.

## v0.2.2 (2021-05-08)
### Fixes
- Fixed bug which prevented parsing settings with multiple valid types.

## v0.2.1 (2021-05-01)
### Features
- `DJANGO_PROJECT` environment variable is now optional. django-envconfig will attempt to infer the project name.
- `DATABASES` now has a default SQLite database generated with the correct `BASE_DIR` if it is not set in the environment or settings.py.
### Fixes
- Ensure that default `BASE_DIR` setting has correct type (`str` in older versions of Django).

## v0.2.0 (2021-04-30)
### Features
- `DJANGO_PROJECT` environment variable is now optional. django-envconfig will attempt to infer the project name.
- `DATABASES` now has a default SQLite database generated with the correct `BASE_DIR` if it is not set in the environment or settings.py.
### Fixes
- Ensure that default `BASE_DIR` setting has correct type (`str` in older versions of Django).

## v0.1.3 (2021-04-14)
### Features
- Added support for new Django minor version 3.2.

## v0.1.2 (2020-11-21)
### Features
- Added support for all Django versions that support Python 3.6+ to date including the following minor versions: 1.11, 2.0, 2.1, 2.2.
- Load custom settings from environments by defining them first in settings.py with a default.
### Fixes
- Fix bug in how ImproperlyConfigured exception messages are generated.
- Fix how octal and hex numbers are parsed i.e. numbers prepended with `0o` and `0x` are converted to integers correctly. Used by setting FILE_UPLOAD_PERMISSIONS.
- Ensure that all built-in Django settings that are nullable can be set to `None`.
- Use non-deprecated database backend module for PostgreSQL.

## v0.1.1 (2020-11-20)
### Features
- Search in potential project root paths to find a `.env` file, which are guessed based on command-line arguments.
### Fixes
- Fix bug which prevented py36 and py37 support (i.e. use of the Python walrus operator).
