
class InvalidCommand(Exception):
    """Exception raised when a command isn't valid."""

    def __init__(self, cmd):
        self.cmd = cmd
        super().__init__(f"Invalid command: {cmd}")


class BadCommandUse(Exception):
    """Exception raised when a command is used incorrectly."""

    def __init__(self, cmd):
        self.cmd = cmd
        super().__init__(f"Invalid use of command: {cmd}")


class TooFewArguments(Exception):
    """Exception raised when a command has too few arguments."""

    def __init__(self, cmd):
        self.cmd = cmd
        super().__init__(f"Too few arguments for command: {cmd}")


class TooManyArguments(Exception):
    """Exception raised when a command has too many arguments."""

    def __init__(self, cmd):
        self.cmd = cmd
        super().__init__(f"Too many arguments for command: {cmd}")
