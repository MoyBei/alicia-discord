from alicia_core.command import register_command
from .hello import hello

register_command("$hello", hello)