from Basketball import FanDuel
from selenium import webdriver
import mysql.connector
from importantInfo import matchups
from importantInfo import databaseRet
import threading
from datetime import *


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Gocubsgo19!!!",
    database="oddsDB"
)

mycursor = db.cursor()



def gettingTeams(gameID):

    # Getting the name of the away team for this game
    query = "SELECT awayTeam FROM matchups WHERE gameID = %s"
    vals = (gameID,)
    mycursor.execute(query,vals)
    awayTeam = mycursor.fetchall()

    # Getting the name of the home team for this game
    query = "SELECT homeTeam FROM matchups WHERE gameID = %s"
    vals = (gameID,)
    mycursor.execute(query, vals)
    homeTeam = mycursor.fetchall()

    # The '*' and the index are only there because fetchall() returns a tuple, and I just want the pure value of the teams

    # print(*homeTeam[0])
    # print(*awayTeam[0])

    return (*homeTeam[0], *awayTeam[0])
#JUST USED FOR TESTING PURPOSES
#homeTeam, awayTeam = gettingTeams(45587)

"""
This function will get the spread data from the database given a team name and the gameId
for the game that is in question. It querys the database for the most recent data
that has been added to it, as this function will be useful when trying to display the live data 
for games that are going on.

Each query is getting two pieces of information. The spread for that sportsbook, and the odds that are associated
with that spread. The fetchall() tuple will return two values, the first being the spread itself, 
and the second will be the odds for that spread

Two different queries are necessary because the search requirments differ in the slightest amount which 
makes it require its own query.
"""
def gettingSpreadInfo(gameID, teamName):

    # getting the FanDuel spread for team that is passed in
    query = "SELECT FDspread,fdspreadOdds FROM spreads WHERE gameID = %s AND team = %s AND FDspread IS NOT NULL ORDER BY timeTaken DESC LIMIT 1"

    vals = (gameID, teamName)
    mycursor.execute(query, vals)
    fanDuelSpread = mycursor.fetchall()

    # getting the DraftKings spread for the team that is passed in

    query = "SELECT DKspread, DKspreadodds FROM spreads WHERE gameID = %s AND team = %s AND DKspread IS NOT NULL ORDER BY timeTaken DESC LIMIT 1"
    vals = (gameID, teamName)
    mycursor.execute(query, vals)
    dkSpread = mycursor.fetchall()

    # This returns the spread and then the odds for that spread - In this same order as stated
    # The fetchall returns a list of tuples. There is only one list - but there are two elements in the list
    # that is why the indexing is the way that it is - in the format "list '0' element '0'/'1'
    return (fanDuelSpread[0][0], fanDuelSpread[0][1], dkSpread[0][0], dkSpread[0][1])

# BOTH FOR TESTING PURPOSES
# fd, fdOdds, dk, dkOdds = gettingSpreadInfo(82927, "Boston Celtics")
# print(fd)
# print(fdOdds)
# print(dk)
# print(dkOdds)

def gettingMoneyLineInfo(gameID):

    # Getting the Home and Away Team moneyline for games that are on fanduel - they will be fetched in that same order
    query = "SELECT homeTeamMoney, awayTeamMoney FROM moneyline WHERE gameID = %s AND homeTeamMoney IS NOT NULL ORDER BY timeTaken DESC LIMIT 1"
    vals = (gameID,)
    mycursor.execute(query, vals)
    fanduelMoneyLines = mycursor.fetchall()

    # Getting the Home and Away TEam moneyline for games that are on draftKings - they will be fetched in that same order
    query = "SELECT dkHomeTeamMoney, dkAwayTeamMoney FROM moneyline WHERE gameID = %s AND dkHomeTeamMoney IS NOT NULL ORDER BY timeTaken DESC LIMIT 1"
    vals = (gameID,)
    mycursor.execute(query, vals)
    dkMoneylines = mycursor.fetchall()

    return (fanduelMoneyLines[0][0], fanduelMoneyLines[0][1], dkMoneylines[0][0], dkMoneylines[0][1])

# FOR TESTING PURPOSES
# fdHome, fdAway, dkHome, dkAway = gettingMoneyLineInfo(40371)
# print(fdHome)
# print(fdAway)
# print(dkHome)
# print(dkAway)

def gettingOverUnder(gameID):

    query = 'SELECT fdOver, fdOverOdds, fdUnder, fdUnderOdds FROM overunder WHERE gameID = %s AND fdOver IS NOT NULL ORDER BY timeTaken DESC LIMIT 1'
    vals = (gameID,)
    mycursor.execute(query, vals)
    fdOverUnder = mycursor.fetchall()

    query = 'SELECT dkOver, dkOverOdds, dkUnder, dkUnderOdds FROM overunder WHERE gameID = %s AND fdOver IS NOT NULL ORDER BY timeTaken DESC LIMIT 1'
    vals = (gameID,)
    mycursor.execute(query, vals)
    dkOverUnder = mycursor.fetchall()

    return (fdOverUnder[0][0], fdOverUnder[0][1], fdOverUnder[0][2], fdOverUnder[0][3], dkOverUnder[0][0], dkOverUnder[0][1], dkOverUnder[0][1], dkOverUnder[0][1])




def gettingGameDate(gameID):
    # this query will get the date the game is supposed to take place
    query = "SELECT date FROM matchups WHERE gameID = %s"

    vals = (gameID,)
    mycursor.execute(query, vals)
    date = mycursor.fetchall()

    print(date)
