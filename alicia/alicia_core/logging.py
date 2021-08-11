from enum import Enum


class LogType(Enum):
  INFO = 1
  WARNING = 2
  ERROR = 3
  CRITICAL = 4


def log(type, message):
  if (type == LogType.INFO):
    print(f"[Info] {message}")
  elif (type == LogType.WARNING):
    print(f"[Warn] {message}")
  elif (type == LogType.ERROR):
    print(f"[Err]  {message}")
  elif (type == LogType.CRITICAL):
    print(f"[Crit] {message}")
  