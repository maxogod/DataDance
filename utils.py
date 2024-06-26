from state.global_state import GlobalState
from defs import *


supported_commands = {
    "cm <normal/database_path>": "change mode to normal or a database \n\t\t(normal mode is the default)\n\t\t(if database_path doesn't exist, create it)",
    "import <csv_file_path> (<database_path>) (<table_name>)": "import a csv file into a database, provide db and table name optionally",
    "sql <sql_command>": "execute a SQL command",
    "save": "commits changes to the database",
    "ls": "list databases",
    "rm <database_path>": "remove a database",
    "clear": "clear the screen",
    "help": "prints help message. You can use it with a command like 'help import'",
    "exit": "exit the program",
    # graph bar table x y -- and other graphs
}


def graceful_exit():
    GlobalState.ask_for_save_confirmation()
    GlobalState.enter_normal_mode()


def is_db_file(file: str) -> bool:
    return file.split(".")[-1] in DB_EXTENSIONS
