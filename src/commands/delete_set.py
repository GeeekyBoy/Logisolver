import nlp
from constants import TxtColors


def delete_set(command: str, avail_sets: dict[str, list[str]]) -> None:
    """
     Permanently deletes an already defined set.

     Parameters:
         command (str): Delete command from which entities will be extracted.
         avail_sets (dict[str, list[str]]): A dictionary of all defined sets.
    """
    # Extract entities of the command.
    entities: list[str] = nlp.get_entities(command, "DELETE")
    # Read name of set to be deleted from the extracted entities.
    set_name: str = entities[0].upper()
    # Check if the set in question is the universal set.
    if set_name == "S":
        # Inform user that it is prohibited to delete the universal set.
        print(TxtColors.FAIL + 'Deleting sample space is not allowed.' + TxtColors.DEFAULT)
    # Check if the set in question is not defined.
    elif not avail_sets[set_name]:
        # Inform user that undefined sets can not be deleted.
        print(TxtColors.FAIL + "Set '" + set_name + "' does not exist." + TxtColors.DEFAULT)
    else:
        # Delete the entry of the set in question from avail_sets.
        del avail_sets[set_name]
