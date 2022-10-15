import subprocess

from utils import run_command

from bump2release import colorama_handler, constants, exceptions


def get_current_version():
    try:
        with open(constants.DEFAULT_VERSION_FILE) as f:
            version = f.read().strip()
    except FileNotFoundError:
        exceptions.MissingVersionFile(f"No '{constants.DEFAULT_VERSION_FILE}' file found in directory")
    return version


def bumpversion_config_exists() -> bool:
    try:
        with open(constants.BUMP2VERSION_CONFIG):
            pass
    except FileNotFoundError:
        return False
    return True


def run_bump2version(version_part: str, target_file: str = None, tag_message: str = None, commit=False):
    cmd = f"{constants.BUMP2_VERSION_CLI} {version_part}"
    if target_file:
        cmd += f" {target_file}"
    if commit:
        cmd += " --commit"
    if tag_message:
        cmd += f' --tag --tag-message "{tag_message}"'
    print(f"Bump2version Command: '{cmd}'")
    try:
        print(run_command(cmd))
    except subprocess.CalledProcessError as e:
        raise exceptions.Bump2VersionError(f"Issue running Bump2version. stderr: {e.stderr}, output: {e.output}")

    except Exception as e:
        raise exceptions.Bump2VersionError(f"Issue running Bump2version. {type(e).__name__}: {str(e)}")


def bump_commit_tag_flow(version_part, tag_message: str, config_exists=False) -> str:
    """Run the underlying bump2version cli, return updated version"""
    target_file = constants.DEFAULT_VERSION_FILE if not config_exists else None
    before_version = get_current_version()
    colorama_handler.print_yellow_header("bump-commit-tag")
    run_bump2version(version_part, target_file=target_file, tag_message=f"({{now:%d.%m.%Y}}) - {tag_message}", commit=True)
    after_version = get_current_version()
    if before_version == after_version:
        exceptions.FailedVersionIncrement(f"Bump2Version action failed. Version is still {before_version}")
    colorama_handler.print_green(f"bumped version: {before_version} --> {after_version}")
    return after_version
