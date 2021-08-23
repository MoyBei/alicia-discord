async def calc(message, client):
    calc_str = message.content.replace("$calc ", "")
    try:
        answer = eval(calc_str)
        await message.channel.send(f"Calculate: {calc_str} = {answer}")
    except (TypeError, KeyError, NameError):
        await message.channel.send(f"`$calc [what to calculate]`")
