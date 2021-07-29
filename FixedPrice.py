#Fixed Price DKP
import sqlite3

conn = sqlite3.connect('Roster.db')
cur = conn.cursor()

roster = 'SELECT Player, DKP from Roster'

for row in cur.execute(roster):
    print(row)