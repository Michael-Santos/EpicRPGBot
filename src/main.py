import os
from dotenv.main import dotenv_values, find_dotenv, load_dotenv

from Browser import Browser


def load_config():
    return {
        **dotenv_values(find_dotenv()),
        **os.environ
    }


if __name__ == '__main__':
    config = load_config()

    browser = Browser(config)
    browser.login()
    browser.go_to_channel()
    browser.send_chat_command("rpg chop")
    pass
