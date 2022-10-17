from unittest.mock import patch

import pytest

from bump2release import exceptions
from bump2release.utilities import git_actions

SUBPROCESS_PATCH_PATH = "bump2release.utilities.git_actions.run_command"


def test_dirty_check():
    with pytest.raises(exceptions.DirtyGitStaging):
        with patch(target=SUBPROCESS_PATCH_PATH, autospec=True, return_value="\ndirty_file1.py\ndirty_file2.py"):
            git_actions.check_if_dirty()


def test_invalid_branch():
    with pytest.raises(exceptions.InvalidBranchError):
        git_actions.validate_branch("feature2")


def test_valid_branch():
    git_actions.validate_branch("main")
