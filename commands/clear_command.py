from commands.command import Command
from errors import TooManyArguments


class ClearCommand(Command):
    """
    clears the screen
    """

    def __init__(self, args: list[str]):
        if args:
            raise TooManyArguments("clear")

    def execute(self):
        print("\033[H\033[J", end="")
