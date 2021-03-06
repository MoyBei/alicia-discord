# Alicia is born on 09 August 2021

from pathlib import Path
import discord
import logging
import datetime
import importlib

import alicia_core
from alicia_core.config import read_config, write_empty_config_json
from alicia_core.logging import LogType, log
from alicia_core.command import execute_command
from alicia_core.message_trigger import trigger_registered_functions


# >------------------initializing bot------------------<
def start_bot():
    """Starting the bot and return current_config"""
    # error logging
    logging.basicConfig(level=logging.ERROR)
    log(LogType.INFO, "Starting up ...")
    config_path = Path.cwd() / "config.json"
    log(LogType.INFO, f"Reading configuration file from current directory ({config_path})")

    chosen_config = None
    try:
        chosen_config = read_config(config_path)
        return chosen_config
    except IOError as e:
        log(LogType.ERROR, str(e))

        write_empty_config_json(config_path)

        log(LogType.INFO, "Empty configuration file generated.")
        log(LogType.INFO, "Please enter your token in the configuration file and restart Alicia.")

        exit(-1)
    except KeyError as e:
        log(LogType.ERROR, str(e))

        exit(-2)


alicia_core.current_config = start_bot()
# importing modules specified in the config
for module_name in alicia_core.current_config.modules:
    importlib.import_module(f"modules.{module_name}")

# >------------------bot loaded------------------<

# starting the client
client = discord.Client()


@client.event  # register async event
async def on_ready():
    log(LogType.INFO, "The bot is ready.")
    log(LogType.INFO, f"Logged in as {client.user}.")


@client.event
async def on_message(message):
    if message.author == client.user:  # to skip when the message author is bot itself
        return

    await trigger_registered_functions(message, client)

    if message.content.startswith("$"):
        await execute_command(message.content.split(" ", 1)[0], message, client)


log(LogType.INFO, "Connecting to Discord...")
# put this at the end
client.run(alicia_core.current_config.token)
