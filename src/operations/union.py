__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"


def union(first_set: list[str], second_set: list[str]) -> list[str]:
    """
     Concatenates two list-based sets and returns the resulted set.

     Parameters:
         first_set (list[str]): The first set.
         second_set (list[str]): The second set.

     Returns:
         (list[str]): A list-based set containing all elements found in the two sets.
     """
    result: list[str] = []
    for i in first_set:
        if i not in result:
            result.append(i)
    for i in second_set:
        if i not in result:
            result.append(i)
    return result
