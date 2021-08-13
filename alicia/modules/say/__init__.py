from alicia_core.command import register_command
from .say import say

register_command("$say", say)