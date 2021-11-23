#Connects the SQL DB to the bot.
'''
ToDO
standardise inputs
create better table
'''

import sqlite3

con = sqlite3.connect("UWAESDB.db") #connects to database

cursor = con.cursor() #cursor is used to navigate database



def CreateTable():
    #Function to create table as is
    cursor.execute("CREATE TABLE Users (DiscordID INTEGER, IsMember INTEGER, StudentID INTEGER, Name TEXT, PRIMARY KEY(DiscordID))")
    con.commit()

def InsertUser(DiscordID, IsMember, StudentID, Name):
    #TODO duplicate protection logic
    cursor.execute("INSERT INTO Users (DiscordID, IsMember, StudentID, Name) VALUES (?,?,?,?)", (DiscordID, IsMember, StudentID, Name))
    con.commit()

def EditUser(DiscordID, Collumn, Input):
    #TODO make sure user exists first
    #cursor.execute("UPDATE Users SET " + str(Collumn) + " = ? WHERE DiscordID = ?", (DiscordID, Input))
    cursor.execute("UPDATE Users SET " + str(Collumn) + " = ? WHERE DiscordID = ?", (Input, DiscordID))
    con.commit()









def FetchRiotID(DiscordID):
    RiotID = cursor.execute("SELECT RiotID FROM Users WHERE DiscordID = " + str(DiscordID))
    return(cursor.fetchall()[0][0])

def FetchRiotName(DiscordID):
    RiotID = cursor.execute("SELECT RiotName FROM Users WHERE DiscordID = " + str(DiscordID))
    return(cursor.fetchall()[0][0])

InsertUser(22222222, 0, 22709039, "Max Stoner")
#EditUser(22709039, "DiscordID", 11111111)