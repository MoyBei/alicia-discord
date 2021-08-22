import discord
from random import randint


async def winlose5050(message, client):
    message_lower = message.content.lower()
    if ("win" in message_lower or "lose" in message_lower) and ("5050" in message_lower or "50/50" in message_lower):
        win_lose = randint(0, 1)
        if win_lose == 0:
            embed_message = discord.Embed(title="Oh no! You lose the 50-50!",
                                          url="https://tenor.com/view/qiqi-genshin-impact-qiqi-shy-shy-loli-gif"
                                              "-18690579")
            await message.channel.send(embed=embed_message)
            await message.channel.send("https://tenor.com/view/qiqi-genshin-impact-qiqi-shy-shy-loli-gif-18690579")

        elif win_lose == 1:
            embed_message = discord.Embed(title="Oh gratz! You win the 50-50!",
                                          url="https://tenor.com/view/baal"
                                              "-raiden-shogun-electro-archon"
                                              "-genshin-impact-burst-gif-22453979")
            await message.channel.send(embed=embed_message)
            await message.channel.send("https://tenor.com/view/baal-raiden-shogun-electro-archon-genshin-impact-burst"
                                       "-gif-22453979")











