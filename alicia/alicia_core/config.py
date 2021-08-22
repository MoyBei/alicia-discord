from pathlib import Path
import json


class AliciaConfig:
    def __init__(self, token):
        self.token = token
        self.modules = []


def read_config(config_path):
    if (Path.exists(config_path)):
        config_dict = json.load(Path.open(config_path))

        if "token" not in config_dict:
            raise KeyError("`token` not set in configuration file.")
        
        config = AliciaConfig(config_dict['token'])

        if "modules" not in config_dict:
            raise KeyError("`modules` not set in configuration file.")

        config.modules = config_dict['modules']

        if "owners" not in config_dict:
            raise KeyError("`owners` not set in configuration file.")

        config.owners = config_dict['owners']

        return config

    else:
        raise IOError("Config file not found.")


def write_empty_config_json(config_path):
    empty_config = AliciaConfig("Enter your token here")
    empty_config.modules = ["Enter your modules here", "Module 1", "Module 2", "..."]
    empty_config.owners = ["Enter bot owner(s) here"]
    config_json = json.dumps(empty_config.__dict__, indent="\t")
    Path.write_text(config_path, config_json)
