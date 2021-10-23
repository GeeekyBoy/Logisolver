__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"


def intersection(first_set: list[str], second_set: list[str]) -> list[str]:
    """
     Finds the common elements between two list-based sets.

     Parameters:
         first_set (list[str]): The first set.
         second_set (list[str]): The second set.

     Returns:
         (list[str]): A list-based set containing the common elements.
     """
    result: list[str] = []
    for i in first_set:
        if i not in result and i in second_set:
            result.append(i)
    return result
