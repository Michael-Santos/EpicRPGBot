import os
from dotenv.main import dotenv_values, find_dotenv, load_dotenv

from Browser import Browser
from EpicRPG import EpicRpg


def load_config():
    return {
        **dotenv_values(find_dotenv()),
        **os.environ
    }

def get_epic_rpg():
    config = load_config()

    browser = Browser(config)
    return EpicRpg(config, browser)

if __name__ == '__main__':
    
    epic_rpg = get_epic_rpg()
    pass
