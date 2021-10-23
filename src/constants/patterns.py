__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

import re
from typing import Pattern

intents: dict[str, Pattern[str]] = {
    "SET": re.compile(r"{((\s*(('(\\'|[^'])*?')(\s*,\s*)?)*('(\\'|[^'])*?')\s*)|\s*)}"),
    "ASSIGNMENT": re.compile(r"(\w)\s*=\s*(.*)"),
    "DELETE": re.compile(r"DELETE (\w)", re.IGNORECASE)
}

entities: dict[str, Pattern[str]] = {
    "SET": re.compile(r"'((?:\\'|[^'])*?)'"),
    "ASSIGNMENT": re.compile(r"(\w)\s*=\s*(.*)"),
    "DELETE": re.compile(r"DELETE (\w)", re.IGNORECASE)
}

other: dict[str, Pattern[str]] = {
    "EXP_SPLITTER":
        re.compile(r"((?:{(?:(?:\s*(?:(?:'(?:\\'|[^'])*?')(?:\s*,\s*)?)*(?:'(?:\\'|[^'])*?')\s*)|\s*)})|(?:\s+))")
}
