__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

import nlp


def parse_set(readable_set: str) -> list[str]:
    """
     Converts a stringified set into its list-based parsed form.

     Parameters:
         readable_set (str): Set represented by the ordinary set notation.

     Returns:
         (list[str]): A list of elements of the provided set.
     """
    return list(map(lambda x: x.replace("\\'", "'"), nlp.get_entities(readable_set, "SET")))
