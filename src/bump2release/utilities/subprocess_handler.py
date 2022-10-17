import subprocess


def run_command(cmd) -> str:
    """ send subprocess command and return decoded string output """
    return subprocess.check_output(cmd, shell=True).decode(encoding="utf-8")


