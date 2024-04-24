from commands.command import Command
from state.global_state import GlobalState
from errors import TooManyArguments, TooFewArguments, BadCommandUse
import utils
import os


class RemoveCommand(Command):
    """
    removes database
    """

    database_to_remove = ""

    def __init__(self, args: list[str]):
        if len(args) < 1:
            raise TooFewArguments("rm <database_path>")
        if len(args) > 1:
            raise TooManyArguments("rm <database_path>")

        if GlobalState.in_db_mode():
            raise BadCommandUse(
                "You must be in normal mode to remove a database")

        if not utils.is_db_file(args[0]):
            raise BadCommandUse("File is not a database")

        self.database_to_remove = args[0]

    def execute(self):
        os.remove(self.database_to_remove)
