__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

import utils
from constants import ExpLabels, supported_operators


def evaluate(parsed_exp: list[list[str]], avail_sets: dict[str, list]) -> list[str]:
    """
     Evaluates the value of a logical expression after parsing it with the parse.

     Parameters:
         parsed_exp (list[list[str]]): Postfix version of the expression returned by parse_exp().
         avail_sets (dict[str, list]): A dictionary of all defined sets.

     Returns:
         (list[str]): The evaluated value in the form of a parsed set.
     """
    # Stack used to evaluate the postfix version of the expression.
    result_stack: list[list] = []
    # Use the well-known algorithm of solving postfix expressions.
    for labeled_token in parsed_exp:
        label, token = labeled_token
        if label == ExpLabels.SET:
            result_stack.append(utils.parse_set(token))
        elif label == ExpLabels.SET_POINTER:
            result_stack.append(avail_sets[token])
        elif label == ExpLabels.UNARY_OPERATOR:
            first_operand = result_stack.pop(-1)
            result_stack.append(supported_operators[token]["operations"](avail_sets["S"], first_operand))
        elif label == ExpLabels.BINARY_OPERATOR:
            first_operand = result_stack.pop(-1)
            second_operand = result_stack.pop(-1)
            result_stack.append(supported_operators[token]["operations"](first_operand, second_operand))
    # Return the first item in the stack which is the desired result after sorting it.
    result_stack[0].sort()
    return result_stack[0]
