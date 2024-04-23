from commands.command import Command
from state.global_state import GlobalState
from errors import TooManyArguments, TooFewArguments, BadCommandUse


class ListCommand(Command):
    """
    lists databases
    """

    def __init__(self, args: list[str]):
        if args:
            raise TooManyArguments("ls")

    def execute(self):
        pass
