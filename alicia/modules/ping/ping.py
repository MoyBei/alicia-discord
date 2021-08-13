async def ping(message, client):
    time_received = message.created_at
    msg2 = await message.channel.send("Pong!")
    ping_a = msg2.created_at - time_received
    ping_b = ping_a.microseconds
    calculated_ping = ping_b / 1000
    await msg2.edit(content=f"Pong! | {calculated_ping} ms")