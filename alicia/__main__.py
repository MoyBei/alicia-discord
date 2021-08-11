from pathlib import Path
import discord
import logging
import datetime
import importlib

# from alicia_core import commands_list
from alicia_core.config import read_config, write_empty_config_json
from alicia_core.logging import LogType, log
from alicia_core.command import execute_command


# print(commands_list)
# error logging
logging.basicConfig(level=logging.ERROR)
log(LogType.INFO, "Starting up ...")
config_path = Path.cwd() / "config.json"
log(LogType.INFO, f"Reading configuration file from current directory ({config_path})")

current_config = None
try:
    current_config = read_config(config_path)
except IOError as e:
    log(LogType.ERROR, str(e))

    write_empty_config_json(config_path)

    log(LogType.INFO, "Empty configuration file generated.")
    log(LogType.INFO, "Please enter your token in the configuration file and restart Alicia.")

    exit(-1)
except KeyError as e:
    log(LogType.ERROR, str(e))

    exit(-2)

# importing modules specified in the config
for module_name in current_config.modules:
    importlib.import_module(module_name)

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

    if message.content.startswith("$"):  
        await execute_command(message.content.split(" ", 1)[0], message)

    elif "miku" in message.content and "ball" in message.content:
        embed_message = discord.Embed(title="This is a Miku Ball! =P", url="https://i.imgur.com/Xc1tP0o.gif")
        embed_message.set_image(url="https://i.imgur.com/Xc1tP0o.gif")
        await message.channel.send(embed=embed_message)


log(LogType.INFO, "Connecting to Discord...")
# put this at the end
client.run(current_config.token)
