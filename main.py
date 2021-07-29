from discord.ext import commands
import os
from dotenv import load_dotenv
from db import *
from LeagueHandler import *

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
async def setlolaccount(ctx, arg1):
    ID = UsernameToID(arg1)
    if (ID == "Summoner name not valid"):
        await ctx.message.channel.send("Oops! Something went wrong. Did you input your username correctly?")
    else:
        editUser(str(ctx.message.author.id), "RiotID", ID)
        await ctx.message.channel.send("League of Legends account set to: "+ arg1)


bot.run(os.getenv("DISCORD_TOKEN"))