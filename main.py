from discord import client
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from db import *
from LeagueHandler import *
import RiftChamps

load_dotenv()

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print("we have logged in as {0.user}".format(bot))

@bot.command(name="register")
async def register(message):
    insertUser(str(message.author.id))
    await message.channel.send("registered")

@bot.command(name="setlolaccount")
async def setlolaccount(ctx, *args):
    Username = ""
    for arg in args:
         Username += (" " + arg)
    ID = UsernameToID(Username)
    if (ID == "Summoner name not valid"):
        await ctx.message.channel.send("Oops! Something went wrong. Did you input your username correctly?")
    else:
        editUser(str(ctx.message.author.id), "RiotID", ID)
        editUser(str(ctx.message.author.id), "RiotName", Username)
        await ctx.message.channel.send("League of Legends account set to: "+ Username)

@bot.command(name="RiftChampsStart")
async def RiftChampsLobbySetup(message):
    await message.channel.send("react to be added to the rift champs lobby!")

@bot.command(name="RiftChampsMakeGames")
async def RiftChampsMakeGames(ctx, msgID):
    message = await ctx.message.channel.fetch_message(msgID)
    reactions = message.reactions
    IDlist = []
    for reaction in reactions:
        async for user in reaction.users():
            IDlist.append(user.id)
    
    Players = []
    for i in range(len(IDlist)):

        DiscordName = await bot.fetch_user(IDlist[i])  #wierd syntax maybe
        DiscordName = DiscordName.display_name
        RiotID = FetchRiotID(IDlist[i])
        RiotName = FetchRiotName(IDlist[i])
        
        Rank = GetRank(RiotID)
        print(Rank)
        RankValue = 1200
        if Rank[0] == "C":
            RankValue += 1300
        if Rank[0] == "G":
            RankValue += 1250
        if Rank[0] == "M":
            RankValue += 1200
        if Rank[0] == "D":
            RankValue += 1000
        if Rank[0] == "P":
            RankValue += 800
        if Rank[0] == "G":
            RankValue += 600
        if Rank[0] == "S":
            RankValue += 400
        if Rank[0] == "B":
            RankValue += 200
        if Rank[0] == "I":
            RankValue += 0
        
        if Rank[-1] == "1":
            RankValue += 150
        if Rank[-1] == "2":
            RankValue += 100
        if Rank[-1] == "3":
            RankValue += 50
        if Rank[-1] == "4":
            RankValue += 0



        # Player object holds all necessary information on each person that reacted
        Player = {"DiscordName" : DiscordName, "RiotName" : RiotName, "RankValue" : RankValue}
        Players.append(Player)
    GameList = RiftChamps.MakeGames(Players)
    MatchCount = 0
    while len(GameList) != 0:
        if len(GameList) >= 2:
            print(GameList)
            MatchCount += 1
            Team1 = GameList.pop(0)
            Team2 = GameList.pop(0)
            Team1String = "Team 1 Players:\n"
            Team2String = "Team 2 Players\n"
            
            for Player in Team1:
                Team1String += "\nDiscord: " + str(Player["DiscordName"]) + " - League of Legends:" + str(Player["RiotName"]) + " - Rank Value:" + str(Player["RankValue"])

            for Player in Team2:
                Team2String += "\nDiscord: " + str(Player["DiscordName"]) + " - League of Legends:" + str(Player["RiotName"]) + " - Rank Value:" + str(Player["RankValue"])

            embed=discord.Embed(
                title=("Match " + str(MatchCount)),
                url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                description=(Team1String + "\n\n" + Team2String),
                color=0xFF5733)
            await ctx.send(embed=embed)
        
        else:
            print(GameList)
            MissedPlayers = GameList.pop(0)
            MissedPlayerString = "These players sadly missed out on a lobby:\n"

            for Player in MissedPlayers:
                MissedPlayerString += "\nDiscord: " + str(Player["DiscordName"]) + " - League of Legends:" + str(Player["RiotName"]) + " - Rank Value:" + str(Player["RankValue"])
        
            embed=discord.Embed(
                title=("Missed Players"),
                url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                description=(MissedPlayerString),
                color=0xFF5733)
            await ctx.send(embed=embed)








bot.run(os.getenv("DISCORD_TOKEN"))

sampletable = [[1, "SantyMax", 2000],[2, "SantyMax2", 2250],[3, "SantyMax3", 2000],[4, "SantyMax4", 1600],[5, "SantyMax5", 1400],[6, "SantyMax6", 1200],[7, "SantyMax7", 2500],[8, "SantyMax8", 1600],[9, "SantyMax9", 2250],[10, "SantyMax10", 2450]]