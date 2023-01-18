from importantInfo import matchups
from selenium import webdriver
import mysql.connector
import Basketball.FanDuel as fd
import time as t
from selenium.webdriver.common.by import By
from datetime import *





driver = webdriver.Chrome("C:/ProjectV2/venv/Scripts/chromedriver.exe")

fd1 = fd.FanDuel(driver)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Gocubsgo19!!!",
    database="oddsDB"
)

mycursor = db.cursor()

"""
One of the goals of this function is be able to schedule its run time - it will run
at pre-determined times of the day and will continue to do so. 

Utilizes the 'gettingMatchupURL' function - which is responsible for getting all URL's available for 
the given sport. 
This function will then be able to check the database and see if the game has already been provided with 
a corresponding URL - and if so... will do nothing. But if no URL had been given to the game for further use
the function will update that matchup row with the correct URL to the game
 
"""

def updateURL(cursor, driver):

    listOfURLs, listOfGameID = gettingMatchupURL(driver, mycursor, db)

    # Need to get the name of the teams that are playing
    # I only want to update the database - if that game doesn't already have a URL there


    for i in range(len(listOfURLs)):
        # THIS QUERY WILL CHECK FOR THAT SPECIFIC GAME ID AND WHETHER THE URL FIELD IS NULL - DETERMINING WHAT TO DO NEXT
        checkNullQuery = "SELECT * FROM matchups WHERE gameID = %s AND url IS NULL"  # it wll be a random gameID that is being given to the database
        value = (listOfGameID[i])  # This will be the variable of gameID - that is retrieved via a function
        cursor.execute(checkNullQuery, (value,))
        result = cursor.fetchall()

        updateQuery = "UPDATE matchups SET url = (%s) WHERE gameID = %s"
        values = (listOfURLs[i], listOfGameID[i])  # the first value here is what is being inserted and it is going at the location of the given gameID
        if (len(result) == 1):
            cursor.execute(updateQuery, values)
            db.commit()
        else:
            print("No need to insert a value")


# COPIED THIS FUNCTION IN FROM 'MATCHUPS.PY' - I THINK THAT IT BELONGS BETTER HERE, AND IT
# HELPS GET RID OF ANY DOUBLE DEPENDENCIES THAT THERE WERE INVOLVING FANDUEL.PY  ----- THIS CHANGE HAS BEEN
# PARTIALLY IMPLEMENTED - BUT NO TESTS HAVE BEEN RUN TO SEE THE FUNCTIONALITY
"""
This function will be capable of retrieving the link to each game that is available on FanDuel
It will find and scrape the game URL (as all games are unique each day) - and it will then utilize
the function to get the gameID and append the URL to the 'matchups' table in the database - as long as 
it doesn't already exist. This will be used by the main program in order to retrieve all data desired
"""
def gettingMatchupURL(driver, cursor, db):
    driver.get("https://sportsbook.fanduel.com/navigation/nba")  # this can be edited as need be - especially for scale of program - if other sports were to be added - corresponding info would need changed as well
    driver.maximize_window()
    allLinks = driver.find_elements(By.CSS_SELECTOR, "a[href*='/basketball/nba']")  # list of all links that were found

    # Creating fanduel basketball object - because this function must check if a game is live or not to decide
    # what needs to be done
    fd1 = fd.FanDuel(driver)

    gameURLlist = []
    gameIDList = []
    for i in range(1, len(allLinks), 2):        # Each link is found twice - that is the reason for the incrementation

        allLinks = driver.find_elements(By.CSS_SELECTOR, "a[href*='/basketball/nba']")
        allLinks[i].click()
        t.sleep(5)

        live = fd1.live(driver)
        if (live == 1):
            # This means that the game is live
            awayTeam = driver.find_element_by_xpath(
                "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span").get_attribute("innerHTML")
            homeTeam = driver.find_element_by_xpath(
                "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div/div[3]/div/div/div[1]/div[3]/div/div/div/div/span").get_attribute("innerHTML")


        else:
            awayTeam = driver.find_element_by_xpath(
                "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span").get_attribute("innerHTML")

            homeTeam = driver.find_element_by_xpath(
                "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div/div[3]/div/div/div[1]/div[3]/div/div/div/div/span").get_attribute("innerHTML")

        gameID = matchups.gettingGameID(cursor, homeTeam, awayTeam, str(date.today()))  # Getting the gameID given the team names

        gameIDList.append(gameID)


        gameURLlist.append(driver.current_url)    # will not need this soon because of database implementation
        driver.back()
    return gameURLlist, gameIDList


# This function call is what needs to be put on a schedule to make everything run as efficient as possible
# The best position for this scheduled function call is probably in the main file - where the program is always
# running and always gathering data... and it can be added there when that is completed
updateURL(mycursor,driver)