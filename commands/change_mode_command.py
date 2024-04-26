from commands.command import Command
from state.global_state import GlobalState
from errors import TooFewArguments, TooManyArguments, BadCommandUse
import utils
from defs import NORMAL_MODE_STR


class ChangeModeCommand(Command):
    """
    Uses:

    > cm normal

    > cm <database_path> (if it doesnt exist, create it)
    """

    mode: str = ""

    def __init__(self, args: list[str]):
        if len(args) < 1:
            raise TooFewArguments("change_mode (cm)")
        if len(args) > 1:
            raise TooManyArguments("change_mode (cm)")

        if not args[0]:
            raise BadCommandUse("cm <normal/database_path>")

        if args[0].split(".")[-1] == "csv":
            raise BadCommandUse(
                "To use csv files first convert them to db using the `import` command")
        elif not utils.is_db_file(args[0]) and not args[0] == NORMAL_MODE_STR:
            raise BadCommandUse(
                f"The file `{args[0]}` isn't a database")

        self.mode = args[0]

    def execute(self):
        GlobalState.enter_db_mode(self.mode)
        print(f"Mode changed to <{self.mode}>")
