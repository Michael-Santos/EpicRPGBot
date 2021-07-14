import os
import time
from dotenv.main import dotenv_values, find_dotenv
import schedule

from Browser import Browser
from EpicRPG import EpicRpg


def load_config():
    print("Loading configs")
    return {
        **dotenv_values(find_dotenv()),
        **os.environ
    }

def get_epic_rpg(config):
    browser = Browser(config)
    return EpicRpg(config, browser)

def execute_all(epic_rpg):
    epic_rpg.chop()
    epic_rpg.fish()
    epic_rpg.heal()
    epic_rpg.adventure()
    epic_rpg.hunt()
    epic_rpg.daily()
    epic_rpg.weekly()

if __name__ == '__main__':
    config = load_config()
    epic_rpg = get_epic_rpg(config)
    execute_all(epic_rpg)

    schedule.every(6).minutes.do(epic_rpg.chop)
    schedule.every(8).minutes.do(epic_rpg.fish)
    schedule.every(30).minutes.do(epic_rpg.adventure)
    schedule.every(3).minutes.do(epic_rpg.hunt)
    schedule.every(20).minutes.do(epic_rpg.heal)
    schedule.every(1).days.do(epic_rpg.daily)
    schedule.every(1).week.do(epic_rpg.weekly)

    while True:
        schedule.run_pending()
        time.sleep(1)
