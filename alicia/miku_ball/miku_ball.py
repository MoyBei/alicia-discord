import discord

async def miku_ball(message):
    if "miku" in message.content and "ball" in message.content:
        embed_message = discord.Embed(title="This is a Miku Ball! =P", url="https://i.imgur.com/Xc1tP0o.gif")
        embed_message.set_image(url="https://i.imgur.com/Xc1tP0o.gif")
        await message.channel.send(embed=embed_message)