from defs import *
import sqlite3


class GlobalState:
    """This class is a singleton that stores the global state of the program."""

    mode = Mode.NORMAL
    open_db = ""
    connection = None
    cursor = None
    unsaved_changes = False

    prompt = "\033[1;34m[normal]\033[0m$ "

    @staticmethod
    def enter_normal_mode():
        if GlobalState.mode == Mode.IN_DATABASE and GlobalState.cursor is not None and GlobalState.connection is not None:
            GlobalState.cursor.close()
            GlobalState.connection.close()
        GlobalState.mode = Mode.NORMAL
        GlobalState.open_db = ""
        GlobalState.unsaved_changes = False
        GlobalState.update_prompt()
        GlobalState.connection = None
        GlobalState.cursor = None

    @staticmethod
    def enter_db_mode(database_path: str):
        if database_path == NORMAL_MODE_STR:
            GlobalState.enter_normal_mode()
            return
        # TODO change between dbs
        try:
            GlobalState.connection = sqlite3.connect(database_path)
        except sqlite3.Error as e:
            print(e)
            GlobalState.enter_normal_mode()
            return
        GlobalState.mode = Mode.IN_DATABASE
        GlobalState.open_db = database_path
        GlobalState.unsaved_changes = False
        GlobalState.update_prompt()
        GlobalState.cursor = GlobalState.connection.cursor()

    @staticmethod
    def in_db_mode():
        return GlobalState.mode == Mode.IN_DATABASE

    @staticmethod
    def in_normal_mode():
        return GlobalState.mode == Mode.NORMAL

    @staticmethod
    def update_prompt():
        if GlobalState.mode == Mode.IN_DATABASE:
            GlobalState.prompt = f"\033[1;34m[{GlobalState.open_db}]\033[0m$ "
        else:
            GlobalState.prompt = "\033[1;34m[normal]\033[0m$ "
