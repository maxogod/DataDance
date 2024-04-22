# ~~~~~~~~~~ CONSTANT VARIABLES DEFINITION ~~~~~~~~~~ #
from enum import Enum

HELP_COMMANDS = ["help", "h", "?", "-h"]

NORMAL_MODE_STR = "normal"


class CommandActions(Enum):
    CHANGE_MODE = "cm"
    SAVE = "save"
    SQL = "sql"


class Mode(Enum):
    NORMAL = 0
    IN_DATABASE = 1
