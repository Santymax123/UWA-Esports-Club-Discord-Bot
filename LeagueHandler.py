from requests.models import HTTPError
from riotwatcher import LolWatcher, ApiError
import os
from dotenv import load_dotenv
from db import *

load_dotenv()

watcher = LolWatcher(os.getenv("Riot_Key"))

region = "OC1"
  

def GetPlayerID(SummonerName): #Can't figure out how to negate the downside of 2 requests but oh well, I'll keep to a sign-up basis
    try:
        summoner = watcher.summoner.by_name(region, SummonerName)
    except HTTPError:
        return("Summoner name not valid")
    except:
        return("Unknown error")
    return([summoner["id"]])

def GetPlayerRank(SummonerID):
    try:
        i = ManualRankList[0].index(SummonerID)
    except:
        try:
            summonerStats = watcher.league.by_summoner(region, SummonerID)
        except HTTPError:
            return([550])
        except:
            return("Unknown Error")
        HighestRank = -1
        for response in summonerStats:
            RankValue = -1
            tier = response["tier"]
            if tier[0] == "C":
                RankValue += 1201
            elif tier[0] == "G" and tier[1] == "R":
                RankValue += 1201
            elif tier[0] == "M":
                RankValue += 1201
            elif tier[0] == "D":
                RankValue += 1001
            elif tier[0] == "P":
                RankValue += 801
            elif tier[0] == "G":
                RankValue += 601
            elif tier[0] == "S":
                RankValue += 401
            elif tier[0] == "B":
                RankValue += 201
            elif tier[0] == "I":
                RankValue += 1
            rank = summonerStats[0]["rank"]
            if rank == "I":
                RankValue += 150
            elif rank == "II":
                RankValue += 100
            elif rank == "III":
                RankValue += 50
            if RankValue > HighestRank:
                HighestRank = RankValue
        if HighestRank == -1:
            return([550])
        else:
            return([HighestRank])
    else:
        return [ManualRankList[1][i]]

def GetPlayerName(SummonerID):
    try:
        summoner = watcher.summoner.by_id(region, SummonerID)
    except:
        return("Unknown Error")
    return([summoner["name"]])

#List of all players who have a manually set rank for any reason, in form of two lists where the same index is shared between the two lists for one person
ManualRankList = [["XvCTEyAdpXCnj_Sd1i0_xF_9UL2LvwvXK_1RPnlckAZs"], [950]]