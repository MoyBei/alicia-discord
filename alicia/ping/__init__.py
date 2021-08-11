from alicia_core.command import register_command
from .ping import ping

register_command("$ping", ping)