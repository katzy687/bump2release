from bump2release import constants, exceptions
from bump2release.utilities import (
    b2v_handler,
    colorama_handler,
    file_reader,
    git_actions,
)


def bump_commit_tag(version_part, tag_message: str, config_exists=False) -> str:
    """Run the underlying b2v cli, return updated version"""
    target_file = constants.DEFAULT_VERSION_FILE if not config_exists else None
    before_version = file_reader.get_current_version()
    colorama_handler.print_yellow_header("bump-commit-tag")
    b2v_handler.run_b2v(version_part, target_file, tag_message=f"({{now:%d.%m.%Y}}) - {tag_message}")
    after_version = file_reader.get_current_version()
    if before_version == after_version:
        exceptions.FailedVersionIncrement(f"Bump2Version action failed. Version is still {before_version}")
    colorama_handler.print_green(f"bumped version: {before_version} --> {after_version}")
    return after_version


def run_release_flow(version_part: str, release_message: str):
    git_actions.check_if_dirty()
    current_branch = git_actions.get_current_branch()
    git_actions.validate_branch(current_branch)
    print(f"current branch: {current_branch}")
    git_actions.git_pull_latest()
    after_version = bump_commit_tag(version_part, release_message, file_reader.bumpversion_config_exists())
    new_tag = f"v{after_version}"
    git_actions.git_push_atomic(new_tag, current_branch)
