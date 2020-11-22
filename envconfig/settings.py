from os import environ, getenv
import sys

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

from envconfig.dotenv import find_dotenv
from envconfig.parser import EnvParser
from envconfig.setting_types import get_setting_types
from envconfig import utils

extra_paths = utils.find_paths_to_project_root()
load_dotenv(dotenv_path=find_dotenv(extra_paths=extra_paths))

project_name = getenv('DJANGO_PROJECT')
if not project_name:
    raise ImproperlyConfigured("Required environment variable "
                               "'DJANGO_PROJECT' not found.")

# Generate default settings and values from startproject template settings.py
settings = utils.get_template_settings(project_name)
# Load any settings from the project_name.settings module (if it exists)
mod_settings = utils.get_module_settings(project_name)
# Overlay the default template settings with any settings module settings
settings.update(mod_settings)

# Get a lookup of built-in Django settings and their valid types
setting_types = get_setting_types()
# Add any custom settings and their default types
setting_types.update({
    s: [type(mod_settings[s])] for s in mod_settings if s not in setting_types
})

if project_name not in settings['INSTALLED_APPS']:
    settings['INSTALLED_APPS'].append(project_name)

envsetting_names = [s for s in setting_types if s in environ]

for name in envsetting_names:
    val = getenv(name)
    if val:
        try:
            settings[name] = EnvParser.parse(val, *setting_types[name])
        except ValueError as e:
            types_str = "', '".join(t.__name__ for t in setting_types[name])
            raise ImproperlyConfigured(
                f"Environment variable '{name}' incorrectly set. "
                f"Error: {str(e)}. Valid types include: '{types_str}'."
            )

# PostgreSQL
# https://www.postgresql.org/docs/current/libpq-envars.html
if 'DATABASES' not in settings and getenv('PGDATABASE'):
    settings['DATABASES'] = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
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
