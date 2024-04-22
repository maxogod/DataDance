from commands.command import Command
from commands.change_mode_command import ChangeModeCommand
from commands.save_command import SaveCommand
from commands.sql_command import SqlCommand
from errors import *
from defs import *


def process_cmd(cmd: str) -> Command:

    action = cmd.split()[0]
    args = cmd.split()[1:] if len(cmd.split()) > 1 else []

    match action:
        case CommandActions.CHANGE_MODE.value:
            return ChangeModeCommand(args)
        case CommandActions.SAVE.value:
            return SaveCommand(args)
        case CommandActions.SQL.value:
            return SqlCommand(args)
        case _:
            raise InvalidCommand(action)
