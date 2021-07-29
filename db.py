#Handles registration to the bot
#dont allow dupes
#update users?
#https://likegeeks.com/python-sqlite3-tutorial/
# no fakes/logic checking

import sqlite3

con = sqlite3.connect("UWAESdatabase.db") #connects to database

cursor = con.cursor() #cursor is used to navigate database

#cursor.execute("UPDATE Users SET RiotID = 'SantyMax' WHERE DiscordID = 221633274013810688")
#con.commit()

def insertUser(DiscordID):
    cursor.execute("INSERT INTO Users (DiscordID) VALUES (" + DiscordID + " )")
    con.commit()

def editUser(DiscordID, Collumn, Input):
    cursor.execute("UPDATE Users SET " + Collumn + " = '" + Input + "' WHERE DiscordID = " + DiscordID)
    con.commit()