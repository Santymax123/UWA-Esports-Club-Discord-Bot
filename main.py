from discord.ext import commands
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) #find the .env file

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print("we have logged in as {0.user}".format(bot))

@bot.command(name="register")
async def register(message):
    await message.channel.send("registered")


bot.run(os.environ.get("DISCORD_TOKEN"))