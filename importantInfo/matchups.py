"""
This file only will be run one time in order to fill up the matchups table
with the correct schedule for the season. The unique gameID is also given to
each game as well. The ID is checked for its uniqueness as well.
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
from random import randint
import time
from importantInfo import timeTranslator



"""
Will get thet matchups for every game in the season, starting with December of 2022
and every game that will follow it. The games are all listed the same, just on 
different web pages - and they only differ by the month extension that can be seen 
at the end of the URL.  It will also then add to the database table "matchups" by calling the function
"""
def getMatchups(driver, cursor, db):
    monthExtensions = ['december', 'january', 'february', 'march', 'april', 'may', 'june']

    dateList, timeList, awayTeamList, homeTeamList = [], [], [], []

    driver.get("https://www.basketball-reference.com/leagues/NBA_2023_games-may.html")

    # THE DATE BUTTON NEEDS TO BE CLICKED PRIOR TO THE DATA BEING SCRAPED - OTHERQIZE , NOT ALL OF THE DATA CAN BE RETRIEIVED

    # Creating a try loop that will go until there are no more games on the schedule
    counter = 1
    while True:
        try:
            date = driver.find_element_by_xpath("//*[@id='schedule']/tbody/tr[" + str(counter) + "]/th/a").get_attribute("innerHTML")
            date = timeTranslator.timeConverter2(date)
            dateList.append(date)
            time = driver.find_element_by_xpath("//*[@id='schedule']/tbody/tr[" + str(counter) + "]/td[1]").get_attribute("innerHTML")
            timeList.append(time)
            awayTeam = driver.find_element_by_xpath("//*[@id='schedule']/tbody/tr[" + str(counter) + "]/td[2]/a").get_attribute("innerHTML")
            awayTeamList.append(awayTeam)
            homeTeam = driver.find_element_by_xpath("//*[@id='schedule']/tbody/tr[" + str(counter) + "]/td[4]/a").get_attribute("innerHTML")
            homeTeamList.append(homeTeam)
            counter += 1

            # This loop will run until a unique gameID is found
            #gameID = creatingGameID(cursor)
            while True:
                gameID = creatingGameID(cursor)
                if checkingGameID(cursor, gameID):
                    addingToDB(gameID, date, time, awayTeam, homeTeam, cursor, db)
                    break
                else:
                    print("sttuck")

        except NoSuchElementException:
            break
def addingToDB(gameID, dates, times, awayTeam, homeTeam, cursor, db):

    sql = "INSERT INTO matchups (gameID, date, time, awayTeam, homeTeam) VALUES (%s, %s, %s, %s, %s)"
    val = (gameID, dates, times, awayTeam, homeTeam)
    cursor.execute(sql, val)
    db.commit()

"""
This function is used to determine if the given gameID exists already 
We do not want to have two matching gameID's, as they are supposed to be 
the unique identifier for all games
If the ID does not exist, the function will return true - saying that it is okay to use that ID
If the ID DOES exist - false will be returned, indicating that another ID should be 
generated 
"""
def checkingGameID(cursor,id):

    query = "SELECT * FROM matchups WHERE gameID = " + id
    cursor.execute(query)
    rows = cursor.fetchall()

    if (len(rows)==0):
        return True
    return False

"""
This function will create a unique gameID for the given matchup - by generating a random 5 digit number
It is called in the getMatchups function when records are being inserted
into the table. This function will call checkingGameID to ensure that the 
ID being given is truly unique and does not already exist in the given set of games
"""
def creatingGameID(cursor):

    low = 10**4
    high = (10**5) - 1

    return str(randint(low, high))


"""
This function will be able to go in and retreive the gameID from the matchups table
and it will return the corresponding gameID based on the data that is provided for it
It will be used to update the tables used for the different markets of the games
Searching for the data will be used given the name of the home team, away team - 
and I also think that I will need to use the date because of the importance if uniqueness 

but that will get a little complicated when it comes to live games because there may be some games that 
are the same, and it will become difficult..... SOLUTION - if the game is live, can just use the 
current date for searching the data
"""

def gettingGameID(cursor, homeTeam, awayTeam, date):

    vals = (homeTeam, awayTeam, date)

    query = "SELECT gameID FROM matchups WHERE homeTeam = %s AND awayTeam = %s AND date >= %s"

    cursor.execute(query, vals)
    result = cursor.fetchall()

    # Need to return the value this way because the query returns results of the query
    # in the form of a tuple, and we only want to retrieve the actual value of the
    # the gameID - so this result will be returned
    for results in result:
        #print(results[0])
        return results[0]


def main():
    driver = webdriver.Chrome("C:/ProjectV2/venv/Scripts/chromedriver.exe")

    # NEEDS TO BE UPDATED WITH VALID CREDENTIALS
    db = mysql.connector.connect(
        host="YOUR_HOST",
        user="YOUR_USER",
        passwd="YOUR_PASSWORD",
        database="YOUR_DB_NAME"
    )

    mycursor = db.cursor()

    getMatchups(driver, mycursor, db)


if __name__ == "__main__":
    main()