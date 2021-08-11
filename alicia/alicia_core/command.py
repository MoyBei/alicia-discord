from . import commands_list


class Command:
    def __init__(self, command, function, collect_args=False):
        self.command = command
        self.function = function
        self.collect_args = collect_args


def register_command(command, function, collect_args=False):
    if (command in commands_list):
        print(f"[Error] Command {command} is already registered. Skipping.")
        return

    commands_list.append(Command(command, function, collect_args))
    print(f"[Info]  Registered command {command}.")


def list_commands():
    print("Available commands: ")
    for cmd in commands_list:
        print(f"\t{cmd.command}")
