import sqlite3

con = sqlite3.connect("UWAESdatabase.db") #connects to database

cursorObj = con.cursor() #cursor is used to navigate database
