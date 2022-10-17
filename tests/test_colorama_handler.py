from bump2release.utilities import colorama_handler


def test_colorama_handler():
    print("")
    colorama_handler.print_yellow_header("this is a header")
    colorama_handler.print_red("this is an error message")
    colorama_handler.print_green("this is success")
