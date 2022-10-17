from bump2release.utilities import subprocess_handler
from unittest.mock import patch

SUBPROCESS_PATCH_PATH = "bump2release.utilities.subprocess_handler.run_command"


def test_mock_sub_process():
    """ patching the subprocess wrapper """
    echo_str = 'hello world'
    with patch(target=SUBPROCESS_PATCH_PATH, autospec=True, return_value=echo_str):
        output = subprocess_handler.run_command(f'echo "{echo_str}"')
    print(f"output: {output}")
    assert echo_str in output


def test_sub_process_real():
    """ integration test, really call subprocess """
    echo_str = 'hello world'
    output = subprocess_handler.run_command(f'echo "{echo_str}"')
    print(f"output: {output}")
    assert echo_str in output
