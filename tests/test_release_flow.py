from bump2release import release_flow
from unittest.mock import patch

GET_CURRENT_BRANCH = "bump2release.release_flow.git_actions.get_current_branch"
PULL_LATEST = "bump2release.release_flow.git_actions.git_pull_latest"
BUMP_COMMIT_TAG = "bump2release.release_flow.bump_commit_tag"
CHECK_DIRTY = "bump2release.release_flow.git_actions.check_if_dirty"
GIT_PUSH_ATOMIC = "bump2release.release_flow.git_actions.git_push_atomic"


@patch(target=GIT_PUSH_ATOMIC, autospec=True)
@patch(target=BUMP_COMMIT_TAG, autospec=True, return_value="0.1.1")
@patch(target=PULL_LATEST, autospec=True)
@patch(target=GET_CURRENT_BRANCH, autospec=True, return_value="main")
@patch(target=CHECK_DIRTY, autospec=True)
def test_release_flow(mock_dirty_check, mock_branch, mock_pull_latest, mock_bumped_tag, mock_push_atomic):
    release_flow.run_release_flow(version_part="minor", release_message="This is minor release")
