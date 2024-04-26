from commands.command import Command
from process_cmd import process_cmd
from state.global_state import GlobalState
from defs import EXIT_COMMANDS
import utils


def main():
    cmd = ""
    while True:
        try:
            cmd = input(GlobalState.prompt)
        except EOFError:
            break

        if not cmd:
            continue

        if cmd in EXIT_COMMANDS:
            utils.graceful_exit()
            break

        try:
            command: Command = process_cmd(cmd)
            command.execute()
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    main()
