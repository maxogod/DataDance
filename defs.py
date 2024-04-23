# ~~~~~~~~~~ CONSTANT VARIABLES DEFINITION ~~~~~~~~~~ #
from enum import Enum

NORMAL_MODE_STR = "normal"


class CommandActions(Enum):
    CHANGE_MODE = "cm"
    IMPORT = "import"
    SQL = "sql"
    SAVE = "save"
    LIST = "ls"
    REMOVE = "rm"
    CLEAR = "clear"
    HELP = "help"


class Mode(Enum):
    NORMAL = 0
    IN_DATABASE = 1
