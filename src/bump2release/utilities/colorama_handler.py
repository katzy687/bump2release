from colorama import Fore, Style


def print_green(message: str) -> str:
    print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")


def print_yellow_header(message: str) -> str:
    print(f"=== {Fore.YELLOW}{message}{Style.RESET_ALL} ===")


def print_red(message: str) -> str:
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")
