from commands.command import Command
from process_cmd import process_cmd


def main():
    cmd = ""
    while True:
        try:
            cmd = input("$ ")
        except EOFError:
            break

        if cmd == "exit":
            break

        if not cmd:
            continue

        try:
            command: Command = process_cmd(cmd)
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    main()
