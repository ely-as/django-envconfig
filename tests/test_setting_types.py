import pytest

from envconfig.setting_types import setting_types
from .utils import get_global_settings_types


@pytest.mark.parametrize('name,type_', get_global_settings_types())
def test_against_global_settings_types(name, type_):
    # Tests two things - whether we have defined the setting, and whether
    # the setting types match up
    assert type_ in setting_types[name]
