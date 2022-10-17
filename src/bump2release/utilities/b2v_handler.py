import subprocess
from bump2release import constants, exceptions
from bump2release.utilities.subprocess_handler import run_command


def build_b2v_command(version_part: str, target_file: str, tag_message: str = None, commit: bool = True) -> str:
    """ Build the cli command """
    cmd = f"{constants.BUMP2_VERSION_CLI} {version_part}"
    if target_file:
        cmd += f" {target_file}"
    if commit:
        cmd += " --commit"
    if tag_message:
        cmd += f' --tag --tag-message "{tag_message}"'
    return cmd


def run_b2v(version_part: str, target_file: str = None, tag_message: str = None, commit=True):
    cmd = build_b2v_command(version_part, target_file, tag_message, commit)
    print(f"Bump2version Command: '{cmd}'")
    try:
        run_command(cmd)
    except subprocess.CalledProcessError as e:
        raise exceptions.Bump2VersionError(f"Issue running Bump2version. stderr: {e.stderr}, output: {e.output}")
    except Exception as e:
        raise exceptions.Bump2VersionError(f"Issue running Bump2version. {type(e).__name__}: {str(e)}")
