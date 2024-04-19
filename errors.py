
class InvalidCommand(Exception):
    """Exception raised when a command isn't valid."""

    def __init__(self, cmd):
        self.cmd = cmd
        super().__init__(f"Invalid command: {cmd}")
