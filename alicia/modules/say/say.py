async def say(message, client):
    message_to_send = message.content.replace("$say", "")
    await message.delete()
    await message.channel.send(message_to_send)