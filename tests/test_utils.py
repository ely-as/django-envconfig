from pathlib import Path

from pytest_mock import MockerFixture

from envconfig import utils

PATH_TO_TEST_TEMPLATE = Path(__file__).parent / 'fixtures/testmodule.py-tpl'


def test_get_template_settings_sets_correct_type_for_BASE_DIR(mocker: MockerFixture) -> None:  # noqa: E501
    default_template_settings = utils.import_module_from_file(
        utils.get_path_to_settings_template()
    )
    mocker.patch('envconfig.utils.get_base_dir',
                 return_value=Path('/path/to/base_dir'))
    base_dir = utils.get_template_settings('foobar')['BASE_DIR']
    assert type(default_template_settings.BASE_DIR) == type(base_dir)  # type: ignore  # noqa


def test_target_template_settings_file_exists():
    path = utils.get_path_to_settings_template()
    assert path.exists()


def test_import_module_from_file():
    mod = utils.import_module_from_file(PATH_TO_TEST_TEMPLATE)
    assert mod.FOO == 'bar'


def test_import_module_from_file_with_str():
    mod = utils.import_module_from_file(PATH_TO_TEST_TEMPLATE.as_posix())
    assert mod.FOO == 'bar'
