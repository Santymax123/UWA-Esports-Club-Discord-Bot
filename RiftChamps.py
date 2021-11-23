

def GetRankValue(Player):
    return Player.get("RankValue")

def MakeGames(Players):
    #for now i am cheating and just filtering down the list

    sampletable = [
    {"DiscordName" : 1, "RiotName" : "SantyMax", "RankValue" : 2000},
    {"DiscordName" : 2, "RiotName" : "SantyMax2", "RankValue" : 2250},
    {"DiscordName" : 3, "RiotName" : "SantyMax3", "RankValue" : 2000},
    {"DiscordName" : 4, "RiotName" : "SantyMax4", "RankValue" : 1600},
    {"DiscordName" : 5, "RiotName" : "SantyMax5", "RankValue" : 1400},
    {"DiscordName" : 6, "RiotName" : "SantyMax6", "RankValue" : 1200},
    {"DiscordName" : 7, "RiotName" : "SantyMax7", "RankValue" : 2500},
    {"DiscordName" : 8, "RiotName" : "SantyMax8", "RankValue" : 1600},
    {"DiscordName" : 9, "RiotName" : "SantyMax9", "RankValue" : 2250},
    {"DiscordName" : 10, "RiotName" : "SantyMax10", "RankValue" : 2000},
    {"DiscordName" : 11, "RiotName" : "SantyMax11", "RankValue" : 1200},
    {"DiscordName" : 12, "RiotName" : "SantyMax12", "RankValue" : 2300},
    {"DiscordName" : 13, "RiotName" : "SantyMax13", "RankValue" : 2700},
    {"DiscordName" : 14, "RiotName" : "SantyMax14", "RankValue" : 2600},
    {"DiscordName" : 15, "RiotName" : "SantyMax15", "RankValue" : 2600},
    {"DiscordName" : 16, "RiotName" : "SantyMax16", "RankValue" : 2600},
    {"DiscordName" : 17, "RiotName" : "SantyMax17", "RankValue" : 2600},
    {"DiscordName" : 18, "RiotName" : "SantyMax18", "RankValue" : 2300},
    {"DiscordName" : 19, "RiotName" : "SantyMax19", "RankValue" : 2600},
    {"DiscordName" : 20, "RiotName" : "SantyMax20", "RankValue" : 2600},
    ]
    

    #sort all players
    Players.sort(key=GetRankValue, reverse = True) #change this line to allow lower ranked players a chance to get in lobbies first
    #contains all teams for the night
    Lobby = []

    #hard coded to put the top 10 players into a team till players run out
    #players left over are the players that missed a lobby
    for Player in Players:
        if len(Players) < 10:
            break
        Team1 = [Players[0], Players[3], Players[4], Players[7], Players[9],]
        Team2 = [Players[1], Players[2], Players[5], Players[6], Players[8],]
        Lobby.append(Team1)
        Lobby.append(Team2)
        del Players[0:10]
    
    Lobby.append(Players)
    return(Lobby)


    
    


        
        




sampletable = [
    {"DiscordName" : 1, "RiotName" : "SantyMax", "RankValue" : 2000},
    {"DiscordName" : 2, "RiotName" : "SantyMax2", "RankValue" : 2250},
    {"DiscordName" : 3, "RiotName" : "SantyMax3", "RankValue" : 2000},
    {"DiscordName" : 4, "RiotName" : "SantyMax4", "RankValue" : 1600},
    {"DiscordName" : 5, "RiotName" : "SantyMax", "RankValue" : 1400},
    {"DiscordName" : 6, "RiotName" : "SantyMax", "RankValue" : 1200},
    {"DiscordName" : 7, "RiotName" : "SantyMax", "RankValue" : 2500},
    {"DiscordName" : 8, "RiotName" : "SantyMax", "RankValue" : 1600},
    {"DiscordName" : 9, "RiotName" : "SantyMax", "RankValue" : 2250},
    {"DiscordName" : 10, "RiotName" : "SantyMax", "RankValue" : 2450}
]

MakeGames(sampletable)

