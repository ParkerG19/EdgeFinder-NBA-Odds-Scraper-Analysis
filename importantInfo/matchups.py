from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
from random import randint
import time
#import Basketball.FanDuel as fd
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
    #for i in range(len(monthExtensions)):
    driver.get("https://www.basketball-reference.com/leagues/NBA_2023_games-january.html")

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

    # This should never occur if it is done correctly - as all games should be able to be found - but it is just a fail safe
    # Will check if there are no results - meaning that it could not find this game in the matchups table
    # if (len(result) == 0):
    #     print("Could not find a game with "+ homeTeam + " as the home team and " + awayTeam + " as the away team")
    # else:
    #     print("Got Home team " + homeTeam + " and the away team as " + awayTeam)


    # Need to return the value this way because the query returns results of the query
    # in the form of a tuple, and we only want to retrieve the actual value of the
    # the gameID - so this result will be returned
    for results in result:
        #print(results[0])
        return results[0]

# """
# This function will be capable of retrieving the link to each game that is available on FanDuel
# It will find and scrape the game URL (as all games are unique each day) - and it will then utilize
# the function to get the gameID and append the URL to the 'matchups' table in the database - as long as
# it doesn't already exist. This will be used by the main program in order to retrieve all data desired
# """
# def gettingMatchupURL(driver, cursor, db):
#     driver.get("https://sportsbook.fanduel.com/navigation/nba")
#     driver.maximize_window()
#     allLinks = driver.find_elements(By.CSS_SELECTOR, "a[href*='/basketball/nba']")  # this indicates all the links that were found at the time of looking
#
#     fd1 = fd.FanDuel(driver)
#
#
#
#     gameURLlist = []
#     gameIDList = []
#     for i in range(1, len(allLinks), 2):        # Each link is found twice - that is the reason for the incrementation
#
#         allLinks = driver.find_elements(By.CSS_SELECTOR, "a[href*='/basketball/nba']")
#         allLinks[i].click()
#         time.sleep(5)
#
#         live = fd1.live(driver)
#         if (live == 1):
#             # This means that the game is live
#             awayTeam = driver.find_element_by_xpath(
#                 "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span").get_attribute("innerHTML")
#             homeTeam = driver.find_element_by_xpath(
#                 "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div/div[3]/div/div/div[1]/div[3]/div/div/div/div/span").get_attribute("innerHTML")
#
#
#         else:
#             awayTeam = driver.find_element_by_xpath(
#                 "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span").get_attribute("innerHTML")
#
#             homeTeam = driver.find_element_by_xpath(
#                 "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div/div[3]/div/div/div[1]/div[3]/div/div/div/div/span").get_attribute("innerHTML")
#
#         gameID = gettingGameID(cursor, homeTeam, awayTeam, "NO DATE NOW")  # Getting the gameID given the team names
#
#         gameIDList.append(gameID)
#
#
#         gameURLlist.append(driver.current_url)    # will not need this soon because of database implementation
#         driver.back()
#         # time.sleep(3)
#     return gameURLlist, gameIDList


# DONT THINK THAT i USE THIS FUNCTION - BUT SAFER NOT TO COMPLETELY DELETE UNTIL 100% SURE
# def addingURLs(driver, cursor, db):
#
#     # Need to get the name of the teams that are playing
#     # I only want to update the database - if that game doesn't already have a URL there
#     awayTeam = driver.find_element_by_xpath(
#         "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span")
#     homeTeam = driver.find_element_by_xpath(
#         "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div/div[3]/div/div/div[1]/div[3]/div/div/div/div/span")
#     gameID = gettingGameID(cursor, homeTeam, awayTeam, "NO DATE NOW")  # Getting the gameID given the team names
#
#     # THIS
#     # QUERY WILL CHECK FOR THAT SPECIFIC GAME ID AND WHETHER THE URL FIELD IS NULL - DETERMINING WHAT TO DO NEXT
#     checkNullQuery = "SELECT * FROM matchups WHERE gameID = %s AND url IS NULL"  # it wll be a random gameID that is being given to the database
#     value = (gameID)  # This will be the variable of gameID - that is retrieved via a function
#     cursor.execute(checkNullQuery, (value,))
#     result = cursor.fetchall()
#
#     updateQuery = "UPDATE matchups SET url = (%s) WHERE gameID = %s"
#     values = ("testingURL",
#               gameID)  # the first value here is what is being inserted and it is going at the location of the given gameID
#     if (len(result) == 1):
#         cursor.execute(updateQuery, values)
#         db.commit()
#     else:
#         print("No need to insert a value")


def main():
    driver = webdriver.Chrome("C:/ProjectV2/venv/Scripts/chromedriver.exe")


    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Gocubsgo19!!!",
        database="oddsDB"
    )

    mycursor = db.cursor()

    getMatchups(driver, mycursor, db)

    #gettingMatchupURL(driver, mycursor)

if __name__ == "__main__":
    main()