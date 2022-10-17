from unittest.mock import patch

from bump2release.utilities import subprocess_handler

SUBPROCESS_PATCH_PATH = "bump2release.utilities.subprocess_handler.run_command"


def test_mock_sub_process():
    """Patching the subprocess wrapper"""
    echo_str = "hello world"
    with patch(target=SUBPROCESS_PATCH_PATH, autospec=True, return_value=echo_str):
        output = subprocess_handler.run_command(f'echo "{echo_str}"')
    print(f"output: {output}")
    assert echo_str in output


def test_sub_process_real():
    """Integration test, really call subprocess"""
    echo_str = "hello world"
    output = subprocess_handler.run_command(f'echo "{echo_str}"')
    print(f"output: {output}")
    assert echo_str in output
