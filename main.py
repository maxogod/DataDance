from commands.command import Command
from process_cmd import process_cmd
from defs import HELP_COMMANDS
import utils


def main():
    cmd = ""
    while True:
        try:
            cmd = input("$ ")
        except EOFError:
            break

        if not cmd:
            continue

        if cmd == "exit":
            utils.graceful_exit()
            break

        if cmd == "clear":
            utils.clear_screen()
            continue

        if cmd in HELP_COMMANDS:
            utils.print_help()
            continue

        try:
            command: Command = process_cmd(cmd)
            command.execute()
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    main()
