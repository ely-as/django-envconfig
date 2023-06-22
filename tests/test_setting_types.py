import pytest

from envconfig.setting_types import get_setting_types

from .utils import get_global_settings_types

setting_types = get_setting_types()


@pytest.mark.parametrize("name,type_", get_global_settings_types())
def test_against_global_settings_types(name: str, type_: type) -> None:
    # Tests two things - whether we have defined the setting, and whether
    # the setting types match up
    assert type_ in setting_types[name]
