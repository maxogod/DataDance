from commands.command import Command
from errors import TooManyArguments
from defs import DB_EXTENSIONS
import utils
import os


class ListCommand(Command):
    """
    lists databases
    """

    def __init__(self, args: list[str]):
        if args:
            raise TooManyArguments("ls")

    def execute(self):
        files = os.listdir()
        db_files = [file for file in files if utils.is_db_file(file)]
        if not db_files:
            print("No databases found in the app directory")
            return
        for db in db_files:
            size = self.__get_size_of_db(db)

            print(f" |{size}| - {db}")

    def __get_size_of_db(self, db: str) -> str:
        size = os.path.getsize(db)
        if size < 1024:
            return f"{size}B"
        elif size < 1024**2:
            return f"{size/1024:.2f}KB"
        elif size < 1024**3:
            return f"{size/1024**2:.2f}MB"
        else:
            return f"{size/1024**3:.2f}GB"
