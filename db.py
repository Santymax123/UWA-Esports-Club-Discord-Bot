#Connects the SQL DB to the bot.
'''
ToDO
standardise inputs
create better table
'''

import sqlite3

con = sqlite3.connect("UWAES.db") #connects to database

cursor = con.cursor() #cursor is used to navigate database


def CreateTable():
    cursor.execute("CREATE TABLE RiftChampions (DiscordID INTEGER, IsMember INTEGER CHECK(IsMember == 1 OR IsMember == 0), LoLName TEXT NOT NULL, LoLID TEXT CHECK(length(LoLID) < 64), Rank INTEGER NOT NULL, Points INTEGER, PlayedWith TEXT, PRIMARY KEY(DiscordID))")
    con.commit()

def InsertUser(DiscordID, IsMember, Name, RiotID, Rank):
    cursor.execute("INSERT INTO RiftChampions VALUES ({0}, {1}, '{2}', '{3}', {4}, 0, '')".format(DiscordID, IsMember, Name, RiotID, Rank))
    con.commit()

def EditUser(DiscordID, Attribute, Input):
    cursor.execute("UPDATE RiftChampions SET {0} = {1} WHERE DiscordID = {2}".format(Attribute, Input, DiscordID))
    con.commit()

def Fetch(DiscordID, Attribute):
    cursor.execute("SELECT {0} FROM RiftChampions WHERE DiscordID = {1}".format(Attribute, DiscordID))
    value = cursor.fetchone()
    if value == None:
        return None
    else:
        return value[0]

def FetchAll(Attributes):
    sequence = ""
    for attribute in Attributes:
        sequence += ", {0}".format(attribute)
    cursor.execute("SELECT {0} FROM RiftChampions WHERE IsMember = 1".format(sequence[2:]))
    return cursor.fetchall()