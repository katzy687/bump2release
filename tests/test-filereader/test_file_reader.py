import os.path

import pytest

from bump2release import exceptions
from bump2release.utilities import file_reader


def test_get_version_path():
    version = file_reader.get_current_version()
    print(f"version: {version}")
    assert version == "0.1.0"


def test_local_config_path():
    assert file_reader.bumpversion_config_exists()


def test_relative_path_version():
    version = file_reader.get_current_version(script_dir_path="valid_script")
    print(f"version: {version}")
    assert version == "0.1.1"


def test_full_path():
    assert file_reader.get_current_version(script_dir_path=os.path.join(os.getcwd(), "valid_script"))


def test_missing():
    with pytest.raises(exceptions.MissingVersionFile):
        file_reader.get_current_version(script_dir_path="invalid_script")
