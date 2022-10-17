from bump2release import constants, exceptions
import os


def _get_target_file_path(target_file_name, script_dir_path: str = None) -> str:
    """
    allow passing relative or full path of script parent dir
    defaults to file name for running from current directory
    """
    if script_dir_path:
        file_path = os.path.join(script_dir_path, target_file_name)
    else:
        file_path = target_file_name
    return file_path


def get_current_version(script_dir_path: str = None):
    """ read config from version.txt, can pass full path, or default to relative """
    file_path = _get_target_file_path(constants.DEFAULT_VERSION_FILE, script_dir_path)
    try:
        with open(file_path) as f:
            version = f.read().strip()
    except FileNotFoundError:
        raise exceptions.MissingVersionFile(f"No '{constants.DEFAULT_VERSION_FILE}' file found at path '{file_path}'")
    return version


def bumpversion_config_exists(script_dir_path: str = None) -> bool:
    """ see if .bumpversion.cfg exists """
    file_path = _get_target_file_path(constants.BUMP2VERSION_CONFIG, script_dir_path)
    try:
        with open(file_path):
            pass
    except FileNotFoundError:
        return False
    return True
