from bump2release import git_actions
from bump2release import b2v_handler


def run_release_flow(version_part: str, release_message: str, bump_config_exists: bool):
    current_branch = git_actions.get_current_branch()
    git_actions.validate_branch(current_branch)
    print(f"current branch: {current_branch}")
    git_actions.check_if_dirty()
    git_actions.git_pull_latest()
    after_version = b2v_handler.bump_commit_tag_flow(version_part, release_message, bump_config_exists)
    new_tag = f"v{after_version}"
    git_actions.git_push_atomic(new_tag, current_branch)
