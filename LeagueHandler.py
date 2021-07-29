#gets a dictionary of discord id's and league id's
#then matches into even teams

from requests.models import HTTPError
from riotwatcher import LolWatcher, ApiError
import os
from dotenv import load_dotenv
from db import *

#dict=

load_dotenv()

watcher = LolWatcher(os.getenv("Riot_Key"))

region = "OC1"

def UsernameToID(Summonername):
    try:
        summoner = watcher.summoner.by_name(region, Summonername)
    except HTTPError:
      return("Summoner name not valid")  

    return(summoner["puuid"])