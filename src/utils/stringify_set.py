__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

def stringify_set(parsed_set: list[str]) -> str:
    """
     Converts a parsed set into its stringified form.

     Parameters:
         parsed_set (list[str]): Set represented by a list of strings.

     Returns:
         (list[str]): Set represented by the ordinary set notation.
     """
    # A variable whose value will be returned at the end of the function.
    result: str = "{"
    # Iterate through the elements of the parsed set.
    for item in parsed_set:
        # Add the current element to the stringified set.
        result += "'" + item.replace("'", "\\'") + "'"
        # Check if this iteration is not the last one.
        if item != parsed_set[-1]:
            # Add the separator comma.
            result += ", "
    # Add the trailing curly bracket that indicated the closure of the set.
    result += "}"
    return result
