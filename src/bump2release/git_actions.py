from bump2release.utils import run_command
from bump2release import exceptions
from bump2release import colorama_handler
from bump2release import constants


def check_if_dirty():
    output = run_command("git status --porcelain")
    if output:
        colorama_handler.print_red(output)
        raise exceptions.DirtyGitStaging("Uncommited files. Can't continue release.")
    print("Git staging is clean")


def validate_branch(current_branch: str):
    if current_branch.lower() not in constants.VALID_BRANCHES:
        err_msg = f"{current_branch} is not valid branch for release. Must be on {constants.VALID_BRANCHES}"
        exceptions.InvalidBranchError(err_msg)


def get_current_branch() -> str:
    """
    https://stackoverflow.com/a/12142066
    :return:
    """
    cmd = "git rev-parse --abbrev-ref HEAD"
    current_branch = run_command(cmd).strip()
    return current_branch


def git_pull_latest():
    colorama_handler.print_yellow_header("git pull")
    print(run_command("git pull"))


def git_push_atomic(new_tag: str, curr_branch: str):
    colorama_handler.print_yellow_header("pushing tags with atomic commit")
    cmd = f"git push --atomic origin {curr_branch} {new_tag}"
    print(run_command(cmd))
    colorama_handler.print_green(f"Release Tag '{new_tag}' Pushed")
