from commands.command import Command
from commands.change_mode import ChangeModeCommand
from errors import *
from defs import *


def process_cmd(cmd: str) -> Command:

    action = cmd.split()[0]
    args = cmd.split()[1:]

    match action:
        case CommandActions.CHANGE_MODE.value:
            return ChangeModeCommand(args)
        case _:
            raise InvalidCommand(action)
