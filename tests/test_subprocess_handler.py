from bump2release.utilities import subprocess_handler


def test_sub_process():
    echo_str = 'hello world'
    output = subprocess_handler.run_command(f'echo "{echo_str}"')
    print(f"output: {output}")
    assert echo_str in output
