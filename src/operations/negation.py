__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"


def negation(universal_set: list[str], first_set: list[str]) -> list[str]:
    """
     Finds elements of the sample space that are missing from a list-based set.

     Parameters:
         universal_set (list[str]): The universal set.
         first_set (list[str]): The first set.

     Returns:
         (list[str]): A list-based set containing all elements not found in the given set.
     """
    result: list[str] = []
    for i in universal_set:
        if i not in result and i not in first_set:
            result.append(i)
    return result
