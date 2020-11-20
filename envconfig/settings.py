from os import getenv
import sys

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

from envconfig.dotenv import find_dotenv
from envconfig.parser import EnvParser
from envconfig.setting_types import setting_types
from envconfig import utils

load_dotenv(dotenv_path=find_dotenv())

project_name = getenv('DJANGO_PROJECT')
if not project_name:
    raise ImproperlyConfigured("Required environment variable "
                               "'DJANGO_PROJECT' not found.")

settings = utils.get_template_settings(project_name)
settings.update(utils.get_module_settings(project_name))

if project_name not in settings['INSTALLED_APPS']:
    settings['INSTALLED_APPS'].append(project_name)

for name in settings:
    if val := getenv(name):
        try:
            settings[name] = EnvParser.parse(val, *setting_types[name])
        except ValueError:
            raise ImproperlyConfigured(str(ValueError))

# PostgreSQL
# https://www.postgresql.org/docs/current/libpq-envars.html
if 'DATABASES' not in settings and getenv('PGDATABASE'):
    settings['DATABASES'] = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': getenv('PGDATABASE'),
            'USER': getenv('PGUSER', ''),
            'PASSWORD': getenv('PGPASSWORD', ''),
            'HOST': getenv('PGHOST', ''),
            'PORT': getenv('PGPORT', ''),
            'TEST': {
                'NAME': 'test_' + getenv('PGDATABASE', ''),
            }
        }
    }

# Make all of the settings attributes of this module
for name, val in settings.items():
    setattr(sys.modules[__name__], name, val)
