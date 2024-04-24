from commands.command import Command
from state.global_state import GlobalState
from errors import TooFewArguments, TooManyArguments, BadCommandUse
from commands.save_command import SaveCommand


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

        self.mode = args[0]

    def execute(self):
        GlobalState.enter_db_mode(self.mode)
        print(f"Mode changed to <{self.mode}>")
