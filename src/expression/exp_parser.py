__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

from constants import supported_operators, ExpLabels


def parse(labeled_tokens: list) -> list:
    """
     Parsing the logical expression by converting its infix-based list of labeled tokens to its postfix version.

     Parameters:
         labeled_tokens (list): A list of tokens labeled by the lexer.

     Returns:
         (list): A list of labeled tokens representing the postfix expression.
     """
    # Delete every token labeled as a whitespace.
    labeled_tokens = list(filter(lambda a: a[0] != ExpLabels.SPACE, labeled_tokens))
    # Build the postfix labeled-tokenized list-based expression using the common well-known algorithm.
    parsed_exp: list = []
    operators_stack: list = []
    for labeled_token in labeled_tokens:
        label, token = labeled_token
        # Check if this token is labeled as a sub expression.
        if label == ExpLabels.SUB_EXP:
            # Parse this sub expression recursively and push the result to the parsed_exp.
            parsed_exp.extend(parse(token))
            if len(operators_stack) and operators_stack[-1][0] == ExpLabels.UNARY_OPERATOR:
                parsed_exp.append(operators_stack.pop(-1))
        elif label == ExpLabels.SET or label == ExpLabels.SET_POINTER:
            parsed_exp.append(labeled_token)
            if len(operators_stack) and operators_stack[-1][0] == ExpLabels.UNARY_OPERATOR:
                parsed_exp.append(operators_stack.pop(-1))
        elif label == ExpLabels.UNARY_OPERATOR:
            operators_stack.append(labeled_token)
        # Check if this token is labeled as a binary operator.
        elif label == ExpLabels.BINARY_OPERATOR:
            # Check if the operators stack is empty.
            if not len(operators_stack):
                # Push this operator to the top of the stack.
                operators_stack.append(labeled_token)
            # Check if its priority is higher than that of the operator in top of the stack.
            elif supported_operators[token]["priority"] < supported_operators[operators_stack[-1][1]]["priority"]:
                # Push it to the top of the stack.
                operators_stack.append(labeled_token)
            # Check if its priority is lower than that of the operator in top of the stack.
            elif supported_operators[token]["priority"] >= supported_operators[operators_stack[-1][1]]["priority"]:
                # Pop all operators having a priority higher than or equal to that of the token
                # and push them to the parsed expression.
                while len(operators_stack) and \
                        supported_operators[token]["priority"] >= \
                        supported_operators[operators_stack[-1][1]]["priority"]:
                    parsed_exp.append(operators_stack.pop(-1))
                # Push the current operator to the top of the stack.
                operators_stack.append(labeled_token)
    # Push all of the remaining operators to the parsed expression.
    operators_stack.reverse()
    parsed_exp.extend(operators_stack)
    # Return the result.
    return parsed_exp
