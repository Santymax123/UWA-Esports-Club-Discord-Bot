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

    return(summoner["id"])

def GetRank(id):
  try:
    stats = watcher.league.by_summoner(region, id)
  except HTTPError:
    return("error fetching ranked stats")
  if stats != []:
    tier = stats[0]['tier']
    rank = ""

    if stats[0]['rank'] == "IV":
      rank = "4"
    if stats[0]['rank'] == "III":
      rank = "3"
    if stats[0]['rank'] == "II":
      rank = "2"
    if stats[0]['rank'] == "I":
      rank = "1"

    FullRank = tier + " " + rank
    return(FullRank)
  else:
    return("SILVER 4")
  


#print(GetRank(UsernameToID("SantyMax")))