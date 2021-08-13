from . import commands_dict
from alicia_core.logging import LogType, log


def register_command(command, function):
    if (command in commands_dict):
        log(LogType.ERROR, f"Command `{command}` is already registered. Skipping.")
        return

    log(LogType.INFO, f"Registering command `{command}`.")
    commands_dict[command] = function


async def execute_command(command, message, client):    
    if command in commands_dict:
        await commands_dict[command](message, client)
    else:
        return
    

def list_commands():
    print("Available commands: ")
    for cmd in commands_dict.keys:
        print(f"\t{cmd.command}")