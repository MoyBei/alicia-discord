from alicia_core.command import register_command
from .forex import forex

register_command("$forex", forex)