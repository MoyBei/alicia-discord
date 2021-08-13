import discord


async def miku_ball(message, client):
    message_lower = message.content.lower()
    if "miku" in message_lower and "ball" in message_lower:
        embed_message = discord.Embed(title="This is a Miku Ball! =P", url="https://i.imgur.com/Xc1tP0o.gif")
        embed_message.set_image(url="https://i.imgur.com/Xc1tP0o.gif")
        await message.channel.send(embed=embed_message)