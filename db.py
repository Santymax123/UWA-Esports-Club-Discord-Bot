#Handles registration to the bot
#dont allow dupes
#update users?
#https://likegeeks.com/python-sqlite3-tutorial/
# no fakes/logic checking

import sqlite3

con = sqlite3.connect("UWAESdatabase.db") #connects to database

cursor = con.cursor() #cursor is used to navigate database

def insertUser(DiscordID, StudentNumber):
    cursor.execute("INSERT INTO Users VALUES(" + str(DiscordID) + ", " + str(StudentNumber) + ")")
    con.commit()

insertUser(3, 22709039)