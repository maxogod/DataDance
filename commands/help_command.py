from commands.command import Command
from errors import TooManyArguments
import utils
from defs import CommandActions


class HelpCommand(Command):
    """
    prints a help message
    """

    command = ""

    def __init__(self, args: list[str]):
        if len(args) > 1:
            raise TooManyArguments("help")
        
        if len(args) == 1:
            self.command = args[0]

    def execute(self):
        match self.command:
            case CommandActions.CHANGE_MODE.value:
                print("\033[1;34m\t- cm <normal/database_path>\033[0m: \033[1;32mchange mode to normal or a database \n\t\t(normal mode is the default)\n\t\t(if database_path doesn't exist, create it)\033[0m")
            case CommandActions.IMPORT.value:
                print("\033[1;34m\t- import <csv_file_path> (<database_path>) (<table_name>)\033[0m: \033[1;32m> import a csv file into a database, provide db and tablename optionally\n\t\t> import ex.csv\n\t\t> import ex.csv ex.sqlite3\n\t\t> import ex.csv ex.sqlite3 ex_table_name\033[0m")
            case CommandActions.SAVE.value:
                print("\033[1;34m\t- save\033[0m: \033[1;32mcommits changes to the database\033[0m")
            case CommandActions.SQL.value:
                print("\033[1;34m\t- sql <sql_command>\033[0m: \033[1;32mexecute a SQL command\n\t\tsql SELECT * FROM ex_table\033[0m")
            case CommandActions.LIST.value:
                print("\033[1;34m\t- ls\033[0m: \033[1;32mlist databases\033[0m")
            case CommandActions.REMOVE.value:
                print("\033[1;34m\t- rm <database_path>\033[0m: \033[1;32mremove a database\n\t\trm ex.sqlite3\033[0m")
            case CommandActions.CLEAR.value:
                print("\033[1;34m\t- clear\033[0m: \033[1;32mclear the screen\033[0m")
            case CommandActions.HELP.value:
                print("\033[1;34m\t- help\033[0m: \033[1;32mprints help message. You can use it with a command like 'help import'\033[0m")
            case _:
                print("Commands:")
                for cmd in utils.supported_commands.keys():
                    print(f"\033[1;34m\t- {cmd}\033[0m", end=": ")
                    print(f"\033[1;32m{utils.supported_commands[cmd]}\033[0m")
