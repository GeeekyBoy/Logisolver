from typing import Optional

__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

from constants import patterns


def get_entities(phrase: str, intent: str) -> Optional[list]:
    """
     Extracts entities of a given phrase.

     Parameters:
         phrase (str): The string whose entities needed to be extracted.
         intent (str): Intent of the given phrase to know its context.

     Returns:
         (Optional[list]): A list of all entities extracted from the phrase if any.
     """
    # Check if an intent is provided and if it supports entities extraction.
    if intent and patterns.entities[intent]:
        # Extract all entities found in the phrase.
        found: list = patterns.entities[intent].findall(phrase)
        # Check if entities are returned in the form of a list of tuples.
        if len(found) and type(found[0]) is tuple:
            # Return the first tuple after converting it to a list.
            return list(found[0])
        else:
            # Return the extracted entities.
            return found
    else:
        return None
