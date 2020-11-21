# django-envconfig

![Python](https://img.shields.io/pypi/pyversions/django-envconfig)
![Test](https://github.com/ely-as/django-envconfig/workflows/Test/badge.svg)
![License](https://img.shields.io/pypi/l/django-envconfig)

Configure Django using environment variables. Having a `settings.py` file is
optional.

## Getting started

### Installation
```sh
python -m pip install django-envconfig
```

### Usage
Edit the `manage.py`, `asgi.py` and `wsgi.py` files generated by Django's
`startproject` command and change the following line:
```py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'envconfig.settings')
```

### Minimum configuration
The following environment variable is required:
```sh
export DJANGO_PROJECT=my_project_name
```
In the absence of a `settings.py` file the following environment variables are
required: `ALLOWED_HOSTS` and either `DATABASES` or `PGDATABASE`.

Environments may be stored in an `.env` file. This file can be stored in your
root directory (same as `manage.py`) or anywhere on the path (e.g. virtualenv
directory).

## How it works

Any [Django setting](https://docs.djangoproject.com/en/3.0/ref/settings/) can
be configured as an environment variable.
- To set a boolean: `true|yes|on|1` and `false|no|off|0` (case-insensitive)
- To set `None`: `none|null` (case-insensitive)
- Simple lists of strings can be stored comma-separated e.g. `export ALLOWED_HOSTS=127.0.0.1,localhost`
- Dicts and complex lists should be stored as JSON

Settings are loaded with the following priority (highest first):
1. Environment variables.
2. Settings defined in your projects `settings.py`, if it exists.
3. Settings that *would* be defined by a `settings.py` file generated by
   `startproject`. This should eliminate the need for the file in most
   projects. Two main caveats:
   - The default value for `DEBUG` has been changed to `False`.
   - A `SECRET_KEY` is generated but will not persist between sessions (e.g.
     if you restart your server/process manager). This may or may not be an
     issue depending on your use case - see the
     [Django documentation](https://docs.djangoproject.com/en/dev/ref/settings/#secret-key)
     for more details.

If you are using a PostgreSQL backend you do not need to specify a `DATABASES`
setting if you have set PostgreSQL environment variables - the minimum is
`PGDATABASE`. See the [PostgreSQL docs](https://www.postgresql.org/docs/current/libpq-envars.html)
for more details.
