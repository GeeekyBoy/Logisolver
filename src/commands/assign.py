import expression
import nlp
from constants import TxtColors
from utils import print_exp_errors


def assign(command: str, avail_sets: dict[str, list[str]]) -> None:
    """
     Assigns the value of a logical expression to one of the defined sets or defines a new set.

     Parameters:
         command (str): Assign command from which entities will be extracted.
         avail_sets (dict[str, list[str]]): A dictionary of all defined sets.
    """
    # Extract entities of the command.
    entities: list = nlp.get_entities(command, "ASSIGNMENT")
    # Read name of set to be defined from the extracted entities.
    set_name: str = entities[0].upper()
    # Read logical expression to be evaluated and assigned from the extracted entities.
    exp: str = entities[1]
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
            # Evaluate the value of the parsed expression.
            tokenized_result: list[str] = expression.evaluate(parsed_exp, avail_sets)
            # Check if the set whose value will be changed is the universal set or not.
            if set_name == "S":
                # Inform user that manipulating the universal set is prohibited.
                print(TxtColors.FAIL + 'Modification of sample space is not allowed.' + TxtColors.DEFAULT)
            else:
                # Assign value of the evaluated expression to the set in question.
                avail_sets[set_name] = tokenized_result
