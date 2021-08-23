from alicia_core.command import register_command
from .calc import calc

register_command("$calc", calc)