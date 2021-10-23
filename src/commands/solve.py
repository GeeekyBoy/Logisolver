import expression
from constants import TxtColors
from utils import print_exp_errors, stringify_set


def solve(exp: str, avail_sets: dict[str, list[str]]) -> None:
    """
     Begins the process of evaluating an inputted expression and prints the final result.

     Parameters:
         exp (str): Expression entered freely by the user without any constraints.
         avail_sets (dict[str, list[str]]): A dictionary of all defined sets.
    """
    # Tokenize the received expression to be readable by the program.
    tokenized_exp = expression.tokenize(exp, avail_sets)
    if tokenized_exp != -1:
        # labeling the extracted tokens to be ready for parsing
        labeled_tokens = expression.lexer(tokenized_exp)
        # Check errors found in the query
        errors: list = expression.validate(labeled_tokens, avail_sets)
        # Check if there are any errors found
        if len(errors):
            # Print errors in a user-friendly way.
            print_exp_errors(errors, exp)
        else:
            # Parse the labeled tokens to be ready for evaluation.
            parsed_exp = expression.parse(labeled_tokens)
            # Evaluate the value of the tokenized expression.
            tokenized_result = expression.evaluate(parsed_exp, avail_sets)
            # Convert the tokenized result to its readable form to be understood by the user.
            readable_result = stringify_set(tokenized_result)
            # Print the readable result to the console.
            print(TxtColors.OK_GREEN + readable_result + TxtColors.DEFAULT)
