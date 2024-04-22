from state.global_state import GlobalState
from commands.save_command import SaveCommand


def clear_screen():
    print("\033[H\033[J")


def print_help():
    print("Commands:")
    print("  cm <normal/database_path>: change mode to normal or a database")
    print("  exit: exit the program")
    print("  clear: clear the screen")


def graceful_exit():
    if GlobalState.unsaved_changes:
        save = input("Do you want to save changes? (y/n): ")
        while save not in ["y", "n"]:
            save = input("Do you want to save changes? (y/n): ")
        if save == "y":
            save = SaveCommand([])
            save.execute()

    print("Exiting...")
    GlobalState.enter_normal_mode()
