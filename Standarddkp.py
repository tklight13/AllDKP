#Standard DKP
import sqlite3
#Connect to database
conn = sqlite3.connect('Roster.db')
cur = conn.cursor()

#Get roster from DB
lstPresent = list()
roster = 'SELECT Player, Current_dkp from DKP'
lstroster = list()
for row in cur.execute(roster):
    lstroster.append(row)
print(lstroster)

#Start the raid
raid = False
startraid = input("Type start raid.")
if startraid == "start raid":
    raid = True

#Get input of present members at raid.
    while True:
        present = input("Which members are present today? Or say Done to begin bidding.")
        lstPresent.append(present)
        if present == "Done":
            lstPresent.remove("Done")
            break
print(lstPresent)


cur.execute('DROP TABLE IF EXISTS PresentMemDKP')
cur.execute('''CREATE TABLE PresentMemDKP (Player TEXT, Current_DKP INTEGER)''')
#Database set up for present members and their DKP
for members in lstPresent:
    cur.execute('SELECT Current_DKP FROM DKP WHERE Player = ?', (members,))
    current_dkp = cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO PresentMemDKP (Player, Current_DKP) VALUES ( ?, ? )', (members, current_dkp))
    cur.execute('SELECT * FROM PresentMemDKP ORDER BY Current_DKP')
    conn.commit()
winnerlst = list()
winnerdkp = list()
cur.execute('DROP TABLE IF EXISTS Bids')
cur.execute('''CREATE TABLE Bids (Player TEXT, Bid INTEGER, Current_DKP)''')
#Bidding process
if raid == True:
    while True:
        bid = input("Enter your name and bid or say Raid done:")
#Exit from program when raid is done.
        if bid == "Raid done":
            cur.execute('DELETE FROM PresentMemDKP')
            conn.commit()
            quit()
#Figure out who wins.
        elif bid == "Done":
            cur.execute('SELECT MAX(Bid), Player FROM Bids')
            winner = cur.fetchall()[0:]
            for member in winner:
                winnerlst.append(member)
            print(winnerlst)
            winnername = winner[1]
            winnerbid = winner[0]
            print(winnername)
            print(winnerbid)
            winnerlst.append(winnername)
#Subtract winning bid from current dkp.
            for member in winnerlst:
                cur.execute('SELECT Current_DKP FROM Bids WHERE Player = ?', (member,))
                current_dkp = cur.fetchone()[0]
                current_dkp = int(current_dkp) - int(winnerbid)
                cur.execute('DELETE FROM PresentMemDKP WHERE Player = ?', (member,))
                cur.execute('DELETE FROM DKP WHERE Player = ?', (member,))
                cur.execute('INSERT INTO DKP (Player, Current_dkp) VALUES (?,?)', (member, current_dkp,))
                cur.execute('INSERT INTO PresentMemDKP (Player, Current_dkp) Values (?,?)', (member, current_dkp,))
                cur.execute('DELETE FROM Bids')
                conn.commit()
                print(current_dkp)
                break
        else: 
            bid = bid.split()
            player = bid[0]
            bid = bid[1]
            print(player)
            print(bid)
#Figure out if the player has enough DKP to bid the amount they tried.
            cur.execute('SELECT Current_DKP FROM DKP WHERE Player = ?', (player,))
            current_dkp = cur.fetchone()[0]
            if int(bid) > int(current_dkp):
                print("You don't have that much DKP.")
                continue
#No negative bidding.
            if int(bid) < 0:
                print("You can't bid negative numbers.")
                continue
            cur.execute('INSERT OR IGNORE INTO Bids (Player, bid, Current_DKP) VALUES (?, ?, ?)', (player, bid, current_dkp))
            conn.commit()









