__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

from constants import ExpLabels


def count_operands(labeled_tokens: list, operator_index: int) -> int:
    """
     Count number of operands of an operator.

     Parameters:
         labeled_tokens (list): A list of the expression tokens.
         operator_index (int): Index of the token of the operator in question.

     Returns:
         (int): Number of found operands. It may be 0, 1 or 2.
     """
    operands_count = 0
    # Set the iteration variable to start from the element left to operator.
    i: int = operator_index - 1
    # Iterate from labeled token of index 'i' till the first labeled token.
    while i >= 0:
        # Read the label of the current label token.
        label = labeled_tokens[i][0]
        # Check if this token is a valid operand based on its label
        has_left_operand = label == ExpLabels.SUB_EXP or label == ExpLabels.SET or label == ExpLabels.SET_POINTER
        # Exit the loop if the a left operand is found or if anything other than a whitespace is found.
        if has_left_operand:
            operands_count += 1
            break
        elif label != ExpLabels.SPACE:
            break
        # Decrement the iteration variable.
        i -= 1
    # Set the iteration variable to start from the element right to operator.
    i = operator_index + 1
    # Iterate from labeled token of index 'i' till the last labeled token.
    while i < len(labeled_tokens):
        # Read the label of the current label token.
        label = labeled_tokens[i][0]
        # Check if this token is a valid operand based on its label
        has_right_operand = label == ExpLabels.SUB_EXP or label == ExpLabels.SET or label == ExpLabels.SET_POINTER
        # Exit the loop if the a right operand is found or if anything other than a whitespace is found.
        if has_right_operand:
            operands_count += 1
            break
        elif label != ExpLabels.SPACE:
            break
        # Increment the iteration variable.
        i += 1
    # Return the result
    return operands_count
