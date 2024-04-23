from commands.command import Command
from state.global_state import GlobalState
from errors import TooManyArguments, BadCommandUse


class SaveCommand(Command):
    """
    commits changes to the database
    """

    def __init__(self, args: list[str]):
        if args:
            raise TooManyArguments("save")

    def execute(self):
        if not GlobalState.in_db_mode() or not GlobalState.connection:
            raise BadCommandUse(
                "You must be in a database to save changes")

        GlobalState.connection.commit()
        GlobalState.unsaved_changes = False
        print("Changes saved")
