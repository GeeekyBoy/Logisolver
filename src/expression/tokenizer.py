__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

from typing import Union

from constants import TxtColors, patterns


def tokenize(exp: str, avail_sets: dict[str, list[str]]) -> Union[int, list]:
    """
     Tokenizes a freely typed logical expression to be ready for analysis and processing.

     Parameters:
         exp (str): Logical expression entered directly by the user.
         avail_sets (dict[str, list[str]]): A dictionary of all defined sets.

     Returns:
         (Union[int, list]): A list of tokens including whitespace tokens.
     """
    i: int = 0
    opened_parentheses: int = 0
    tokens: list = [""]
    # Iterate through the string of the logical expression.
    # This loop only groups parentheses.
    # Tokenization will be done at the end of the function.
    while i < len(exp):
        # Check if the current character is an opening parenthesis.
        if exp[i] == "(":
            # Increment number of opened parentheses.
            opened_parentheses += 1
            # Check if this parenthesis is not included inside a higher parenthesis.
            if opened_parentheses == 1:
                # Push a new string element for receiving contents inside the parentheses.
                tokens.append("")
            # This parenthesis is a child of another parenthesis.
            else:
                # Treat it as a normal character till evaluating it with the contents of its parent.
                tokens[-1] += "("
        # Check if the current character is a closing parenthesis.
        elif exp[i] == ")":
            # Decrement number of opened parentheses.
            opened_parentheses -= 1
            # Check if there is no remaining opened parentheses.
            if opened_parentheses == 0:
                # Tokenize the whole string found between the parentheses recursively.
                tokens[-1] = tokenize(tokens[-1], avail_sets)
                # Check if there is more characters to analyze.
                if i < len(exp) - 1:
                    # Push a new string element for receiving characters after the parentheses.
                    tokens.append("")
            # Check if the latest found closing parenthesis was orphan.
            elif opened_parentheses < 0:
                # Inform the user about the case.
                print(TxtColors.FAIL + "Orphan closing parenthesis." + TxtColors.DEFAULT)
                # Return an error code and exit the function.
                return -1
            else:
                # Treat it as a normal character till evaluating it with the contents of its parent.
                tokens[-1] += ")"
        # This character is not a parenthesis.
        else:
            # Add it to the latest string element.
            tokens[-1] += exp[i]
        # Increment the iteration variable.
        i += 1
    # Check id there is any remaining orphan opening parenthesis after consuming the whole expression.
    if opened_parentheses > 0:
        # Inform the user about the case.
        print(TxtColors.FAIL + "Missing closing parenthesis." + TxtColors.DEFAULT)
        # Return an error code and exit the function.
        return -1
    # Reset the iteration variable.
    i = 0
    # Iterate through the indices of the tokens list.
    while i < len(tokens):
        # Check if element k is a string.
        # In fact, being a list means that the element has been tokenized
        # recursively while processing parentheses above.
        if type(tokens[i]) is str:
            # Tokenize this chunk of the expression via the predefined pattern EXP_SPLITTER.
            tokenized_chunk = patterns.other["EXP_SPLITTER"].split(tokens[i])
            # Replace the chunk with its tokens.
            tokens[i:i + 1] = tokenized_chunk
            # Increment the iteration variable.
            i += len(tokenized_chunk)
        else:
            # Increment the iteration variable.
            i += 1
    # Delete any dump tokens resulting from string splitting process.
    tokens = list(filter(lambda a: a != '', tokens))
    # Return the resulted list of tokens.
    return tokens
