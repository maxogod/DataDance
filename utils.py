from state.global_state import GlobalState
from commands.save_command import SaveCommand


supported_commands = {
    "cm <normal/database_path>": "change mode to normal or a database \n\t\t(normal mode is the default)\n\t\t(if database_path doesn't exist, create it)",
    "import <database_path> <csv_file_path>": "import a csv file into a database",
    "sql <sql_command>": "execute a SQL command",
    "save": "commits changes to the database",
    "ls": "list databases",
    "rm <database_path>": "remove a database",
    "clear": "clear the screen",
    "help": "print this message xD",
    "exit": "exit the program",
    # graph bar table x y -- and other graphs
}


def graceful_exit():
    GlobalState.ask_for_save_confirmation()
    GlobalState.enter_normal_mode()
