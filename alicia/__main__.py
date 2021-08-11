from pathlib import Path
import discord
import logging

# from alicia_core import commands_list
from alicia_core.config import read_config, write_empty_config_json
from alicia_core.logging import LogType, log

# print(commands_list)
# error logging
logging.basicConfig(level=logging.ERROR)
log(LogType.INFO, "Starting up ...")
config_path = Path.cwd() / "config.json"
log(LogType.INFO, f"Reading configuration file from current directory ({config_path})")

current_config = read_config(config_path)
if (current_config == None):
    write_empty_config_json(config_path)

    log(LogType.ERROR, "Configuration file not present, and was generated.")
    log(LogType.INFO, "Please enter your token in the configuration file and restart Alicia.")

    exit(-1)


# test functions
async def hello(message):
    await message.channel.send("Hello! I'm Alicia. Currently 16 years old ><~! (76B/56/81)"
                "https://tenor.com/view/traffic-fbi-open-up-raid-gif-13450966")


async def say(message):
    message_to_send = message.content.replace("$say", "")
    await message.delete()
    await message.channel.send(message_to_send)


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

    # if message.content.startswith("$hello"):
    #     await message.channel.send("Hello! I'm Alicia. Currently 16 years old ><~! (76B/56/81)")
    #     await message.channel.send("https://tenor.com/view/traffic-fbi-open-up-raid-gif-13450966")
    #
    # if message.content.startswith("$say"):  # let bot to say and delete my message
    #     message_to_send = message.content.replace("$say", "")
    #     await message.delete()
    #     await message.channel.send(message_to_send)

    if message.content.startswith("$"):  # let bot to say and delete my message
        function_split = message.content.split(" ", 1)  # split input into list seperate by a space
        function_requested = function_split[0].replace("$", "")
        await globals()[function_requested](message)


log(LogType.INFO, "Connecting to Discord...")
# put this at the end
client.run(current_config.token)
