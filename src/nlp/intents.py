__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

from typing import Optional

from constants import patterns


def get_intent(phrase: str) -> Optional[str]:
    """
     Queries the intent of a given phrase.

     Parameters:
         phrase (str): The string whose intent needed to be queried.

     Returns:
         (Optional[str]): Intent of the phrase if any.
     """
    # Iterate through all intents supported by the program.
    for key in patterns.intents:
        # Check if this is the correct intent.
        if patterns.intents[key].match(phrase):
            # Return this intent
            return key
    # Return None to indicate that there is no intent matching the given phrase.
    return None
