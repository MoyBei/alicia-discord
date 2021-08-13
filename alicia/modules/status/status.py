import discord

# Buggy code, please help try to figure how to fix :kappa:


# async def status(message):
#     if message.author.id in current_config.owners:
#         split_content = message.content.split(" ", 2)
#         if len(split_content) != 3:
#             await message.channel.send("$status`space`[playing/streaming/listening/watching]`space`[content]")
#         elif split_content[1] == "playing":
#             await client.change_presence(
#                 activity=discord.Activity(type=discord.ActivityType.playing, name=split_content[2]))
#         elif split_content[1] == "streaming":
#             await client.change_presence(
#                 activity=discord.Activity(type=discord.ActivityType.streaming, name=split_content[2]))
#         elif split_content[1] == "listening":
#             await client.change_presence(
#                 activity=discord.Activity(type=discord.ActivityType.listening, name=split_content[2]))
#         elif split_content[1] == "watching":
#             await client.change_presence(
#                 activity=discord.Activity(type=discord.ActivityType.watching, name=split_content[2]))
#         else:
#             await message.channel.send(
#                 "Invalid parameters... Master, am i too BAKA to understand ur requests? :sob:")
#     else:
#         print(message.author.id)
#         await message.channel.send("You are not my master, I only listen to my master.")
#         await message.channel.send("https://tenor.com/view/kaguya-sama-love-is-war-chika-"
#                                    "fujiwara-laugh-giggle-evil-laugh-gif-17149742")