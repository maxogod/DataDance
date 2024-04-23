from commands.command import Command
from commands.change_mode_command import ChangeModeCommand
from commands.import_command import ImportCommand
from commands.save_command import SaveCommand
from commands.sql_command import SqlCommand
from commands.list_command import ListCommand
from commands.remove_command import RemoveCommand
from commands.clear_command import ClearCommand
from commands.help_command import HelpCommand
from errors import *
from defs import *


def process_cmd(cmd: str) -> Command:

    action = cmd.split()[0]
    args = cmd.split()[1:] if len(cmd.split()) > 1 else []

    match action:
        case CommandActions.CHANGE_MODE.value:
            return ChangeModeCommand(args)
        case CommandActions.IMPORT.value:
            return ImportCommand(args)
        case CommandActions.SAVE.value:
            return SaveCommand(args)
        case CommandActions.SQL.value:
            return SqlCommand(args)
        case CommandActions.LIST.value:
            return ListCommand(args)
        case CommandActions.REMOVE.value:
            return RemoveCommand(args)
        case CommandActions.CLEAR.value:
            return ClearCommand(args)
        case CommandActions.HELP.value:
            return HelpCommand(args)
        case _:
            raise InvalidCommand(action)
