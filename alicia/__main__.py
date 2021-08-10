# testing if it works
# ok so i just try to entered 2nd line
# so whatever i dk will it crash or not, but i tried
import discord


print("Starting up ...")
print("Have you done Seed today?")
client = discord.Client()


@client.event  # register async event
async def on_ready():
    print("The bot is ready.")
    print(f"Logged in as {client.user}.")


@client.event
async def on_message(message):
    if message.author == client.user:  # to skip when the message author is bot itself
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello! I'm Alicia. Currently 16 years old ><~! (76B/56/81)")
        await message.channel.send("https://tenor.com/view/traffic-fbi-open-up-raid-gif-13450966")

    if message.content.startswith("$sayd"):  # let bot to say and delete my message
        message_to_send = message.content.replace("$sayd", "")
        await message.delete()
        await message.channel.send(message_to_send)





# put this at the end
client.run("MjI3NzM3MTU5NDg5MTU5MTY4.V-EOwQ.boqpZAnQngkHFe8RX4vduem6Ca8")
