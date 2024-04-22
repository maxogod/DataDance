from commands.command import Command
from state.global_state import GlobalState
from errors import TooFewArguments, BadCommandUse


class SqlCommand(Command):
    """
    All sql clauses are supported.
    """

    clause: str = ""

    def __init__(self, args: list[str]):
        if len(args) < 1:
            raise TooFewArguments("Write a sql clause")

        self.clause = " ".join(args)

    def execute(self):
        if not GlobalState.in_db_mode() or not GlobalState.cursor:
            raise BadCommandUse(
                "You must be in a database to execute a sql command")

        GlobalState.cursor.execute(self.clause)
        GlobalState.unsaved_changes = True
