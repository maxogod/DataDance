# ~~~~~~~~~~ CONSTANT VARIABLES DEFINITION ~~~~~~~~~~ #
from enum import Enum


class CommandActions(Enum):
    CHANGE_MODE = "cm"


class Mode(Enum):
    NORMAL = 0
    IN_DATABASE = 1
