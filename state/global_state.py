from defs import Mode


class GlobalState:
    """This class is a singleton that stores the global state of the program."""

    mode = Mode.NORMAL

    @staticmethod
    def enter_normal_mode():
        mode = Mode.NORMAL

    @staticmethod
    def enter_db_mode():
        mode = Mode.IN_DATABASE
