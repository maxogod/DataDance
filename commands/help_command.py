from commands.command import Command
from errors import TooManyArguments
import utils


class HelpCommand(Command):
    """
    prints a help message
    """

    def __init__(self, args: list[str]):
        if args:
            raise TooManyArguments("help")

    def execute(self):
        print("Commands:")
        for cmd in utils.supported_commands.keys():
            print(f"\033[1;34m\t- {cmd}\033[0m", end=": ")
            print(f"\033[1;32m{utils.supported_commands[cmd]}\033[0m")
