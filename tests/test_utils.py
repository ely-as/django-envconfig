from pathlib import Path

from envconfig import utils

PATH_TO_TEST_TEMPLATE = Path(__file__).parent / 'fixtures/testmodule.py-tpl'


def test_target_template_settings_file_exists():
    path = utils.get_path_to_settings_template()
    assert path.exists()


def test_import_module_from_file():
    mod = utils.import_module_from_file(PATH_TO_TEST_TEMPLATE)
    assert mod.FOO == 'bar'


def test_import_module_from_file_with_str():
    mod = utils.import_module_from_file(PATH_TO_TEST_TEMPLATE.as_posix())
    assert mod.FOO == 'bar'
