import os


def clear_console() -> None:
    """
     Clears all previously inputted commands.
    """
    # Determine the appropriate clearing command according to the type of the host system.
    command = 'cls' if os.name in ('nt', 'dos') else 'clear'
    # Execute the command.
    os.system(command)
