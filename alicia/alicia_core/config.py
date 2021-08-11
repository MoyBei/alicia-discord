from pathlib import Path
import json


class AliciaConfig:
    def __init__(self, token):
        self.token = token


def read_config(config_path):
    if (Path.exists(config_path)):
        config_dict = json.load(Path.open(config_path))
        return AliciaConfig(config_dict['token'])

    else:
        return None


def write_empty_config_json(config_path):
    config_json = json.dumps(AliciaConfig("Enter your token here").__dict__, indent="\t")
    Path.write_text(config_path, config_json)
