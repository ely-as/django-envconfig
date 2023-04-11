# django-envconfig

[![Test](https://github.com/ely-as/django-envconfig/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/ely-as/django-envconfig/actions/workflows/test.yml)
![License](https://img.shields.io/pypi/l/django-envconfig)

![Django](https://img.shields.io/pypi/djversions/django-envconfig)
![Python](https://img.shields.io/pypi/pyversions/django-envconfig)

Configure Django using environment variables (envvars). `settings.py` optional.

## Getting started

### Installation
```sh
python -m pip install django-envconfig
```

### Usage
Edit the `manage.py`, `asgi.py` and `wsgi.py` files generated by Django's
`startproject` command and modify the following line:
```py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'envconfig.settings')
```

### Minimum configuration
The following envvars are required (if `settings.py` is removed):
- `ALLOWED_HOSTS` (unless you set `DEBUG=on`)

Environments may be stored in an `.env` file. This file can be stored in your
root directory (next to `manage.py`) or anywhere on the path (e.g. virtualenv
directory).

## How it works

Any [Django setting](https://docs.djangoproject.com/en/3.2/ref/settings/) can
be configured as an environment variable.
- To set booleans: `true|yes|on|1` and `false|no|off|0` (case-insensitive)
- To set `None`: `none|null` (case-insensitive)
- Simple lists of strings can be stored comma-separated e.g. `export ALLOWED_HOSTS=127.0.0.1,localhost`
- Dicts and complex lists should be stored as JSON

Settings are loaded with the following priority (highest first):
1. Environment variables.
2. Settings defined in your projects `settings.py`, if it exists. Note: any
   custom settings should be defined here with their default value.
3. Settings that *would* be defined by a `settings.py` file generated by
   `startproject`. This should eliminate the need for the file in (2) for most
   projects. Caveats:
   - The default value for `DEBUG` has been changed to `False`.
   - A `SECRET_KEY` is generated but will not persist between sessions (e.g.
     if you restart your server/process manager). Check the
     [Django documentation](https://docs.djangoproject.com/en/dev/ref/settings/#secret-key)
     to see whether you need to set a persistent `SECRET_KEY` as an
     environment variable.

## django-envconfig environment variables

Helper environment variables to use with django-envconfig:

| Environment variable | Description |
| --- | --- |
| `DJANGO_PROJECT` | May be required if django-envconfig cannot find your project. Set to the name of the module originally generated by `startproject` |
| `ADD_INSTALLED_APPS` | Add to [`INSTALLED_APPS`](https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps) |
| `REMOVE_INSTALLED_APPS` | Remove from [`INSTALLED_APPS`](https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps) |
| `ADD_MIDDLEWARE` | Add to [`MIDDLEWARE`](https://docs.djangoproject.com/en/dev/topics/http/middleware/#activating-middleware) |
| `REMOVE_MIDDLEWARE` | Remove from [`MIDDLEWARE`](https://docs.djangoproject.com/en/dev/topics/http/middleware/#activating-middleware) |

### PostgreSQL environment variables

If you are using a PostgreSQL backend you do not need to set `DATABASES`. You
can simply set PostgreSQL environment variables - the minimum is `PGDATABASE`.
See the
[PostgreSQL docs](https://www.postgresql.org/docs/current/libpq-envars.html)
for the full list of envvars. This way the same environment can be used when
calling
[PostgreSQL command line utilities](https://www.postgresql.org/docs/current/reference-client.html)
such as `psql` or `pg_dump`.

## Why

- To separate configuration from code. See
  [The Twelve Factor App](https://12factor.net/).
- Use serverless services such as AWS Lambda and Heroku.
- Avoid having to template settings files and keep the auto-generated
  `settings.py` up to date between Django versions.
- Use .env files for easy switching between environments/deployments
  (e.g. dev, test and prod).

## Dependencies

- [python-dotenv](https://github.com/theskumar/python-dotenv) (BSD 3-clause license)

## License

[MIT](https://github.com/ely-as/django-envconfig/blob/main/LICENSE).
