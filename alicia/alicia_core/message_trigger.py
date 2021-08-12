from . import per_message_trigger_list
from alicia_core.logging import LogType, log

def register_per_message_trigger(function):
    if function not in per_message_trigger_list:
        log(LogType.INFO, f"Registering function `{function.__name__}` to be called on every message.")
        per_message_trigger_list.append(function)
    else:
        log(LogType.ERROR, f"Function `{function.__name__}` is already registered to be called on every message, skipping.")

async def trigger_registered_functions(message):
    for function in per_message_trigger_list:
        await function(message)