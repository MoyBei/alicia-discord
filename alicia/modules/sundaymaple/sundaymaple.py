from pathlib import Path
from alicia_core.logging import LogType, log
import discord


async def sundaymaple(message):
    sundaymaple_file = Path(__file__).parent / "sundaymaple.md"

    messasge_to_send = ""
    if Path(sundaymaple_file).exists():
        messasge_to_send = Path(sundaymaple_file).read_text(encoding="UTF-8")
    else:
        messasge_to_send = "Sunday Maple contents not set! Please notify the bot owners."
        log(LogType.ERROR, f"Sunday Maple contents file ({sundaymaple_file}) not found! Please create it and fill in the contents there.")

    await message.channel.send(messasge_to_send)