__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

from constants import TxtColors


def print_exp_errors(errors: list, exp: str) -> None:
    """
     Takes errors returned by validate_exp() and print them in a user-friendly way.

     Parameters:
         errors (list): List of errors returned by validate_exp().
         exp (str): Expression entered initially by the user.
     """
    # Iterate through each error of the provided errors.
    for error in errors:
        # Print the error message in red.
        print(TxtColors.FAIL + error[0] + TxtColors.DEFAULT)
        # Construct the error trace and underline the part caused the error.
        error_trace = \
            TxtColors.FAIL + exp[:error[1]] + TxtColors.WARNING + TxtColors.UNDERLINE + \
            exp[error[1]:error[2]] + TxtColors.NO_UNDERLINE + TxtColors.FAIL + exp[error[2]:]
        # Print the error trace.
        print(error_trace + TxtColors.DEFAULT)
        # Check if this error is not the last error.
        if errors[-1] != error:
            # Leave a newline.
            print("")
