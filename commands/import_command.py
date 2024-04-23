from commands.command import Command
from state.global_state import GlobalState
from errors import TooManyArguments, TooFewArguments, BadCommandUse


class ImportCommand(Command):
    """
    imports a csv file into a database
    """

    def __init__(self, args: list[str]):
        if len(args) < 2:
            raise TooFewArguments("import <database_path> <csv_path>")
        if len(args) > 2:
            raise TooManyArguments("import <database_path> <csv_path>")

    def execute(self):
        pass
