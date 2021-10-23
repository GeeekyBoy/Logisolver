__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

from typing import Union

import nlp
from constants import ExpLabels, supported_operators


def lexer(tokenized_exp: list) -> list[Union[str, list]]:
    """
     Labels each token tokenized by tokenize_exp() for easier parsing and expression validation.

     Parameters:
         tokenized_exp (list): List of the tokens of the expression.

     Returns:
         (list[Union[str, list]]): A list of labeled tokens including whitespace tokens.
     """
    labeled_tokens: list[Union[str, list]] = []
    # Iterate through the provided list of tokens.
    for token in tokenized_exp:
        # Check if this token is a list which indicates that it was parentheses.
        if type(token) is list:
            # Label it as a sub expression.
            labeled_tokens.append([ExpLabels.SUB_EXP, lexer(token)])
        # Check if this token is a set represented by the ordinary set notation.
        elif nlp.get_intent(token) == "SET":
            # Label it as a set.
            labeled_tokens.append([ExpLabels.SET, token])
        # Check if this token is one of the supported operators.
        elif token.upper() in supported_operators:
            # Label it as its type, either a unary operator or a binary operator.
            labeled_tokens.append([supported_operators[token.upper()]["type"], token.upper()])
        # Check if this token is single English letter.
        elif len(token) == 1 and token.isalpha():
            # Label it a set pointer.
            labeled_tokens.append([ExpLabels.SET_POINTER, token.upper()])
        # Check if this token has no non-whitespace characters.
        elif not len(token.strip()):
            # Label it as a space.
            labeled_tokens.append([ExpLabels.SPACE, token])
        # None of the above conditions is satisfied.
        else:
            # Label this token as unknown.
            labeled_tokens.append([ExpLabels.UNKNOWN, token])
    # Return the list of the labeled tokens.
    return labeled_tokens
