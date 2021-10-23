import sys

from constants import TxtColors


def exit_program() -> None:
    """
     Exits the whole program.
    """
    print(TxtColors.HEADER + "Thanks for using our program!" + TxtColors.DEFAULT)
    print(TxtColors.HEADER + "Wishing you a happy day :)" + TxtColors.DEFAULT)
    sys.exit()
