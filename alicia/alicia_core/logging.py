from enum import Enum
from datetime import datetime


class LogType(Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4


def log(type, message):
    if (type == LogType.INFO):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} [Info] {message}")
    elif (type == LogType.WARNING):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} [Warn] {message}")
    elif (type == LogType.ERROR):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} [Err]  {message}")
    elif (type == LogType.CRITICAL):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} [Crit] {message}")
  