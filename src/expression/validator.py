__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

from typing import Union

import utils
from constants import ExpLabels


def validate(labeled_tokens: list, avail_sets: dict[str, list[str]],
             start_index: int = 0, is_initial: bool = True) -> Union[list, tuple[list, int]]:
    """
     Checks the entered logical expression for errors by analyzing its labeled tokens.

     Parameters:
         labeled_tokens (list): A list of tokens labeled by the lexer.
         avail_sets (dict[str, list[str]]): A dictionary of all defined sets.
         start_index (int): Index of character in the original expression from which validation starts.
         is_initial (bool): A flag determining if the function is called by itself.

     Returns:
         (list): A list of all found errors.
     """
    # The list where every found error will be stored.
    errors: list = []
    # The index of the first character of the next token to be checked.
    # This index is determined according to the original freely-typed expression.
    # It is used to emphasize the token caused the error when printing the error message.
    pointer_index: int = start_index
    # Iterate through the list of the labeled tokens.
    # Enumeration is used here to obtain the labeled token index.
    for index, labeled_token in enumerate(labeled_tokens):
        # Assign the token and its label to separate variables.
        label, token = labeled_token
        # Check if this token is labeled as a sub expression.
        if label == ExpLabels.SUB_EXP:
            # Check if this sub expression has some labeled tokens.
            if len(token):
                # Validate this sub expression recursively.
                sub_exp_errors, last_pointer_index = validate(token, avail_sets, pointer_index + 1, False)
                # Check if some errors were found throughout this sub expression.
                if len(sub_exp_errors):
                    # Add those errors to the main list of errors.
                    errors.extend(sub_exp_errors)
                pointer_index = last_pointer_index + 1
            else:
                # Add the error to the list of errors.
                errors.append(["Illegal empty parentheses", pointer_index, pointer_index + 2])
                pointer_index += 2
        # Check if this token is labeled as a whitespace.
        elif label == ExpLabels.SPACE:
            # Move the pointer forward and skip this loop iteration.
            pointer_index += len(token)
            continue
        # Check if this token is a set pointer.
        elif label == ExpLabels.SET_POINTER:
            # Check if this pointer does not point to any one of the defined sets.
            if token not in avail_sets:
                # Add the error to the list of errors.
                errors.append(["Set '" + token + "' does not exist.", pointer_index, pointer_index + len(token)])
        # Check if this token is labeled as a set.
        elif label == ExpLabels.SET:
            # Parse this set to read its elements.
            parsed_set = utils.parse_set(token)
            # Check if this set has some elements that do not belong to the universal set.
            if not all(x in avail_sets["S"] for x in parsed_set):
                # Add the error to the list of errors.
                errors.append(
                    [token + " is not a subset of the universal set.", pointer_index, pointer_index + len(token)])
        # Check if this token is labeled as a unary operator and does not have one operand.
        elif label == ExpLabels.UNARY_OPERATOR and not utils.count_operands(labeled_tokens, index) == 1:
            # Add the error to the list of errors.
            errors.append(["Operator '" + token + "' takes one operand.", pointer_index, pointer_index + len(token)])
            break
        # Check if this token is labeled as a binary operator and does not have two operands.
        elif label == ExpLabels.BINARY_OPERATOR and not utils.count_operands(labeled_tokens, index) == 2:
            # Add the error to the list of errors.
            errors.append(["Operator '" + token + "' takes two operands.", pointer_index, pointer_index + len(token)])
            break
        # Check if this token is labeled as unknown but does have some operands.
        elif label == ExpLabels.UNKNOWN and utils.count_operands(labeled_tokens, index) > 0:
            # Add the error to the list of errors.
            errors.append(["Operator '" + token + "' is not supported yet.", pointer_index, pointer_index + len(token)])
        # Check if this token is labeled as unknown.
        elif label == ExpLabels.UNKNOWN:
            # Add the error to the list of errors.
            errors.append(["Unexpected token '" + token + "'.", pointer_index, pointer_index + len(token)])
        if type(token) is str:
            pointer_index += len(token)
    # Check if this function is not called by itself.
    if is_initial:
        # Return the list of all found errors.
        return errors
    else:
        # Return a tuple containing the list of all found errors and the pointer index.
        return errors, pointer_index
