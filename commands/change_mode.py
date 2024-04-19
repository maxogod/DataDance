from commands.command import Command
from state.global_state import GlobalState


class ChangeModeCommand(Command):

    def __init__(self, mode):
        # TODO just the mode argument?
        # its actually a list of args
        self.mode = mode

    def execute(self):
        # TODO change between modes
        # GlobalState.enter_db_mode()
        pass
