## v0.4.0 (2024-12-20)
### Breaking Changes
- Dropped support for Python 3.7. End of life for Python 3.7 was 2023-06-27 (see the
  [Status of Python Versions](https://devguide.python.org/versions/)).
- Dropped support for Python 3.8. End of life for Python 3.8 was 2024-10-07 (see the
  [Status of Python Versions](https://devguide.python.org/versions/)).
- Dropped support for Django 1.11, 2.0 and 2.1 since these versions do not support Python 3.9 or higher.

### Features
- Added support for Python 3.13 and Django 5.1 [#21](https://github.com/ely-as/django-envconfig/issues/21) by [@ely-as](https://github.com/ely-as) in [#22](https://github.com/ely-as/django-envconfig/pull/22).

## v0.3.1 (2023-12-06)
### Features
- Added support for Python 3.12 and Django 5.0 [#19](https://github.com/ely-as/django-envconfig/issues/19) by [@ely-as](https://github.com/ely-as) in [#20](https://github.com/ely-as/django-envconfig/pull/20).

## v0.3.0 (2023-06-26)
### Breaking Changes
- Dropped support for Python 3.6. End of life for Python 3.6 was 2021-12-23 (see the
  [Status of Python Versions](https://devguide.python.org/versions/)).

### Fixes
- Added `py.typed` file to indicate that package is type-enabled
  ([f27cd0e](https://github.com/ely-as/django-envconfig/commit/f27cd0e)).

### Internal
- Set the minimum required version of tox to `>=4.0`and used the labels feature to tell
  GitHub Actions which testenvs to run
  ([255bd20](https://github.com/ely-as/django-envconfig/commit/255bd20)).
- Removed `{posargs}` from tox commands
  ([b93de2d](https://github.com/ely-as/django-envconfig/commit/b93de2d)).
- Switched to pyproject.toml for all setuptools and test tool configuration by @ely-as
  in [#14](https://github.com/ely-as/django-envconfig/pull/14).
- Switched from flake8 to ruff for linting and fixed `B904` errors
  ([9007bc7](https://github.com/ely-as/django-envconfig/commit/9007bc7)).
- Began to use isort formatting rules using ruff and added new tox testenv `format`
  ([8600a04](https://github.com/ely-as/django-envconfig/commit/8600a04)).
- Replaced `{toxinidir}` with `{tox_root}` in tox.ini
  ([22a8982](https://github.com/ely-as/django-envconfig/commit/22a8982)).
- Dropped support for Python 3.6 by @ely-as in
  [#17](https://github.com/ely-as/django-envconfig/pull/17).
- Began to use black for code formatting
  ([773c838](https://github.com/ely-as/django-envconfig/commit/773c838)).
- Configured tox to generate JSON coverage reports and GitHub Actions to upload reports
  to cov.ely.as ([b542b1b](https://github.com/ely-as/django-envconfig/commit/b542b1b)).

## v0.2.7 (2023-04-03)
### Features
- Support Django 4.1.7 and 4.2 [#1](https://github.com/ely-as/django-envconfig/issues/1) by [@ely-as](https://github.com/ely-as) in [#4](https://github.com/ely-as/django-envconfig/pull/4).

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
