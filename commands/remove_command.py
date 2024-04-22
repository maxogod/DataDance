from commands.command import Command
from state.global_state import GlobalState
from errors import TooManyArguments, TooFewArguments, BadCommandUse


class RemoveCommand(Command):
    """
    removes database
    """

    def __init__(self, args: list[str]):
        if len(args) < 2:
            raise TooFewArguments("rm <database_path>")
        if len(args) > 2:
            raise TooManyArguments("rm <database_path>")

    def execute(self):
        pass
