#Loot Council
import sqlite3

conn = sqlite3.connect('Roster.db')
cur = conn.cursor()

roster = 'SELECT Player from Roster'

for row in cur.execute(roster):
    print(row)

#DB of roster which includes loot attained and date