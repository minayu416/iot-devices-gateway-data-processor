import os
import json

config_file = "./.env.json"


class Config(object):
    def __load_json(self):
        if not os.path.isfile(config_file):
            return

        with open(config_file, 'r', encoding="utf-8") as json_file:
            json_dict = json.loads(json_file.read())

        for key, item in json_dict.items():
            # dynamic generate config params
            setattr(self, key, item)

    def __init__(self):
        # Load default config file
        self.__load_json()


config = Config()
