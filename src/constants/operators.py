__author__ = "GeeekyBoy"
__copyright__ = "Copyright 2021, GeeekyBoy Studio"
__license__ = "AGPLv3"
__version__ = "1.0.0"

from constants import ExpLabels
from operations import negation, intersection, union

supported_operators = {
    "NOT": {
        "priority": 0,
        "type": ExpLabels.UNARY_OPERATOR,
        "operations": negation
    },
    "AND": {
        "priority": 1,
        "type": ExpLabels.BINARY_OPERATOR,
        "operations": intersection
    },
    "OR": {
        "priority": 2,
        "type": ExpLabels.BINARY_OPERATOR,
        "operations": union
    }
}
