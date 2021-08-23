async def calc(message, client):
    calc_str = message.content.replace("$calc ", "")
    pi_replace_str = calc_str.replace("pi", "3.14159265358979")
    try:
        answer = eval(pi_replace_str)
        await message.channel.send(f"Calculate: {calc_str} = {answer}")
    except (TypeError, KeyError, NameError):
        await message.channel.send(f"`$calc [what to calculate]`")
