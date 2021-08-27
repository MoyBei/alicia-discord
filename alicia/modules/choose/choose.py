from random import choice


async def choose(message, client):
    choose_str = message.content.replace("$choose ", "")
    to_choose = choose_str.split(" ")
    try:
        if "$choose" in to_choose:
            raise KeyError
        answer = choice(to_choose)
        await message.channel.send(f"My choice:  {answer}")
    except (TypeError, KeyError, NameError):
        await message.channel.send(f"`$choose [choices separated with space]`")
