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
        if GlobalState.in_db_mode():
            GlobalState.ask_for_save_confirmation()
            GlobalState.close_db()

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

        if GlobalState.in_db_mode():
            GlobalState.ask_for_save_confirmation()
            GlobalState.close_db()

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
        if GlobalState.in_db_mode():
            GlobalState.prompt = f"\033[1;34m[{GlobalState.open_db}]\033[0m$ "
        else:
            GlobalState.prompt = "\033[1;34m[normal]\033[0m$ "

    @staticmethod
    def ask_for_save_confirmation():
        if not GlobalState.in_db_mode() or not GlobalState.connection:
            return
        if GlobalState.unsaved_changes:
            save = input("Do you want to save changes? (y/n): ")
            while save not in ["y", "n"]:
                save = input("Do you want to save changes? (y/n): ")
            if save == "y":
                GlobalState.connection.commit()
                GlobalState.unsaved_changes = False
                print("\033[1;32mChanges saved\033[0m")

    @staticmethod
    def close_db():
        if GlobalState.connection and GlobalState.cursor:
            GlobalState.cursor.close()
            GlobalState.connection.close()
            GlobalState.open_db = ""
            GlobalState.unsaved_changes = False
            GlobalState.update_prompt()
            GlobalState.connection = None
            GlobalState.cursor = None
