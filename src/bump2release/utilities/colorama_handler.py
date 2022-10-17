"""
init() needed
https://stackoverflow.com/a/53564378
"""
from colorama import Fore, Style, init


def print_green(message: str) -> str:
    init()
    print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")


def print_yellow_header(message: str) -> str:
    init()
    print(f"=== {Fore.YELLOW}{message}{Style.RESET_ALL} ===")


def print_red(message: str) -> str:
    init()
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")
