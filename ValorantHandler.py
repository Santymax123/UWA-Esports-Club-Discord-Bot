import os
from dotenv import load_dotenv
from riotwatcher import ValWatcher, RiotWatcher

load_dotenv()

accWatcher = RiotWatcher(os.getenv("Riot_Key"))
valWatcher = ValWatcher(os.getenv("Riot_Key"))