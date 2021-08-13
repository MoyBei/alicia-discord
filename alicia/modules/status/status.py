import discord

from alicia_core import current_config


async def status(message, client):
    if message.author.id in current_config.owners:
        split_content = message.content.split(" ", 2)
        if len(split_content) != 3:
            await message.channel.send("Usage instructions:\n`$status [playing/streaming/listening/watching] [content]`")
        elif split_content[1].lower() == "playing":
            await client.change_presence(
                activity=discord.Activity(type=discord.ActivityType.playing, name=split_content[2]))
        elif split_content[1].lower() == "streaming":
            await client.change_presence(
                activity=discord.Activity(type=discord.ActivityType.streaming, name=split_content[2]))
        elif split_content[1].lower() == "listening":
            await client.change_presence(
                activity=discord.Activity(type=discord.ActivityType.listening, name=split_content[2]))
        elif split_content[1].lower() == "watching":
            await client.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name=split_content[2]))
        else:
            await message.channel.send(
                "Invalid parameters... Master, am i too BAKA to understand ur requests? :sob:\n\n" + 
                "Usage instructions:\n`$status [playing/streaming/listening/watching] [content]`")
    else:
        await message.channel.send("You are not my master, I only listen to my master.")
        await message.channel.send("https://tenor.com/view/kaguya-sama-love-is-war-chika-"
                                   "fujiwara-laugh-giggle-evil-laugh-gif-17149742")