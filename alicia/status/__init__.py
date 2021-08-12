from alicia_core.command import register_command
from .status import status

register_command("$status", status)