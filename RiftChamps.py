from random import randint

#Probably use a class per match with methods for getTeam() (returns a list containing each player on that team), and replace() (replaces a parameter player in a team with the second parameter player).
#__init__() should autobalance the teams when created, not sure if I should keep the ranks on the object though for each player though

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
    [1, "SantyMax", 2000],
    [2, "SantyMax2", 2250],
    [3, "SantyMax3", 2000],
    [4, "SantyMax4", 1600],
    [5, "SantyMax5", 1400],
    [6, "SantyMax6", 1200],
    [7, "SantyMax7", 2500],
    [8, "SantyMax8", 1600],
    [9, "SantyMax9", 2250],
    [10, "SantyMax10", 2450]
]

#print(MakeGames(sampletable))

class Matches:
    def __init__(self):
        self.matches = {}
    
    def createMatches(self, allPlayers):
        j = 0
        for i in range((len(allPlayers) // 10)):
            self.matches.update({"Match{0}".format(i+1): createMatch(allPlayers[0:10])})
            for i in range(10):
                allPlayers.pop(0)
            j = i + 1
        if len(allPlayers) >= 5:
            self.matches.update({"Match{0}".format(j+1): [allPlayers[0:5]]})
            for x in range(5):
                allPlayers.pop(0)
        return allPlayers
            

def createMatch(players): #Need to find a better way to matchmake so insanely high ranked players don't end up stomping every time
    match = [[],[]]
    players.sort(reverse=True, key=GetRank)
    for player in players:
        oneOrTwo = randint(1, 2)
        if len(match[0]) == (len(players) // 2):
            match[1].append(player)
        elif len(match[1]) == (len(players) // 2):
            match[0].append(player)
        else:
            if oneOrTwo == 1:
                if getTeamRank(match[0]) > getTeamRank(match[1]):
                    match[1].append(player)
                else:
                    match[0].append(player)
            else:
                if getTeamRank(match[0]) < getTeamRank(match[1]):
                    match[0].append(player)
                else:
                    match[1].append(player)
    return match
        

def replace(match, replacee, replacer):
    for i in range(match[0]):
        if match[0][i][1] == replacee:
            match[0][i] = replacer
    for i in range(match[1]):
        if match[1][i][1] == replacee:
            match[1][i] = replacer
    return match


def getTeamRank(team):
    return sum([player[2] for player in team])

def GetRank(player):
    return player[2]