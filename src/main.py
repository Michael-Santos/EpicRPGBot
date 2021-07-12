import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

username = os.environ.get("EPICRPG_USERNAME")

print(username)