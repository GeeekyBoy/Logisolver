from constants import TxtColors
from utils import stringify_set


def list_avail_sets(avail_sets: dict[str, list[str]]) -> None:
    """
     Lists elements of all defined sets along with their count.
    """
    # Print elements of the universal set.
    print(TxtColors.OK_CYAN + "S = " + stringify_set(avail_sets["S"]) + TxtColors.DEFAULT)
    # Print count of elements of the universal set.
    print(TxtColors.OK_CYAN + "n(S) = " + str(len(avail_sets["S"])) + TxtColors.DEFAULT)
    for key in avail_sets:
        if key != "S":
            print(" ")
            # Print elements of the set labeled as the value of 'Key'.
            print(TxtColors.OK_CYAN + key + " = " + stringify_set(avail_sets[key]) + TxtColors.DEFAULT)
            # Print count of elements of the set labeled as the value of 'Key'.
            print(TxtColors.OK_CYAN + "n(S) = " + str(len(avail_sets[key])) + TxtColors.DEFAULT)
