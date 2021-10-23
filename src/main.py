__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

import commands
import nlp
import utils
from constants import TxtColors


def start_program():
    """
     The entrypoint of the program source code.
    """
    # The dictionary of all sets defined during the lifecycle of the program.
    avail_sets: dict[str, list[str]] = {}
    while True:
        # Read elements of the universal set.
        readable_universal = input("\n" + TxtColors.DEFAULT + "Please enter the elements of the universal set: ")
        # Validate the syntax of the inputted set.
        if nlp.get_intent(readable_universal) == "SET":
            # Parse the inputted set and store it in avail_sets.
            avail_sets["S"] = utils.parse_set(readable_universal)
            break
        else:
            # Inform user that the syntax of the inputted set is invalid.
            print("\n" + TxtColors.FAIL + "Invalid Set!" + TxtColors.DEFAULT)
    # The main loop of the program
    while True:
        # Listen for incoming commands and queries.
        command = input("\n" + TxtColors.DEFAULT + "logisolver(v1.0.0)> ")
        print("")
        # Analyze the incoming command to know its intent.
        # Single word commands don't require analysis.
        command_intent = nlp.get_intent(command) or command.upper()
        # Call the suitable function according to the intent of the received command.
        if command_intent == "ASSIGNMENT":
            commands.assign(command, avail_sets)
        elif command_intent == "DELETE":
            commands.delete_set(command, avail_sets)
        elif command_intent == "LIST":
            commands.list_avail_sets(avail_sets)
        elif command_intent == "CLEAR":
            commands.clear_console()
        elif command_intent == "EXIT":
            commands.exit_program()
        else:
            commands.solve(command, avail_sets)


if __name__ == '__main__':
    start_program()
