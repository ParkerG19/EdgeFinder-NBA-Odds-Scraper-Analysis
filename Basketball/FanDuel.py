from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time as t
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
from importantInfo import matchups
from importantInfo import databaseRet
from datetime import *



# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="Gocubsgo19!!!",
#     database="oddsDB"
# )
#
# mycursor = db.cursor()



class FanDuel():

    def __init__(self):


        # These are the xpaths for the popular page goes in order of away team spread, odds, moneyline, over, odds, and then
        # home team spread, odds, moneyline, under, odds
        self.popularLiveX = ["//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span",  # Away Team Name
                            "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[1]/div[1]/span[1]",
                             "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[1]/div[1]/span[2]",
                             "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[1]/div[2]/span",
                             "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[1]/div[3]/span[1]",
                             "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[1]/div[3]/span[2]",
                             #"//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div/div[3]/div/div/div[1]/div[3]/div/div/div/div/span",   # Home Team Name
                             "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[1]/div[3]/div/div/div/div/span",
                             "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/span[1]",
                             "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/span[2]",
                             "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/span",
                             "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[2]/div[3]/span[1]",
                             "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[2]/div[3]/span[2]"
                             ]
        # These are the xpaths for the pre game odds - goes in the same order as the live xpaths  (updated on 12/23/22)
        self.popularPreGameX = ["//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span",  # Away Team Name
                               "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[1]/div[1]/span[1]", # Away Team Spread
                               "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[1]/div[1]/span[2]", # Away Team Spread Odds
                               "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[1]/div[2]/span",   # Away Team Moneyline
                               "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[1]/div[3]/span[1]", # Over
                               "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[1]/div[3]/span[2]", # Over Odds
                               "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[1]/div[3]/div/div/div/div/span",   # Home Team Name
                               "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/span[1]",  # Home Team Spread
                               "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/span[2]", # Home Team Spread Odds
                               "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/span",  # Home Team Moneyline
                               "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[2]/div[3]/span[1]",  # Under
                               "//*[@id='main']/div/div[1]/div/div[2]/div[4]/ul/li[2]/div/div/div[3]/div/div/div[2]/div[2]/div[3]/span[2]"  # Under Odds
                                ]

    # This function will get the main game lines - this is displayed on the "popular" page of FanDuel ONLY GETTING THE LINES
    # This page is also the first one that appears when the url to a game is pressed - so it will be the
    # URL that is given from getURL method

    # This function will tell me if the game is live or not - and will be determine which xpath to use
    # If this function returns '1' that means that the game is live, else the game is not live
    def live(self, driver):
        liveX = "//*[@id='LiveTag_svg__a']"
        try:
            driver.find_element_by_xpath(liveX)
        except NoSuchElementException:
            return 0
        return 1

    def popular(self, url, driver, db):

        cursor = db.cursor()
        driver.get(url)
        print("we are here")
        # This should open the inspector page - which I think needs to happen in order to load the elements that are
        # on the page - because the page is dynamic. I am not seeing the inspector open - but it doesn't seem like it
        # has to on this computer - it may have to on my laptop becuase that is where I learned that this was a solution
        # to not being able to find the elements that are on the page

        # Don't want to use all of the try loops if I don't have to. I can append to a list and make a dataframe from that information
        isItLive = self.live(driver)

        # dataList will contain all of the information that is gathered from the 'popular' page including the
        # team name, spread, spread odds, moneyline, over, over odds,..... etc - and in that order; starting with the away team
        dataList = []

        #TESTING PURPOSES
        #print(isItLive)

        # Checking to see if the game is live - as that will determine the xpath that I am using
        # After checking to see if it is live - trys to find element and appends to list if it is found
        # if the element cannot be found - that means that the bet is not available - a "NA" value will be appended
        # to the list as that is the value that is put into the database
        if (isItLive == 1):

            for i in range(len(self.popularLiveX)):
                    try:
                        data = driver.find_element_by_xpath(self.popularLiveX[i]).get_attribute("innerHTML")
                        dataList.append(data)
                    except NoSuchElementException:
                        dataList.append("NA")

        else:
            for i in range(len(self.popularPreGameX)):
                    try:
                        data = driver.find_element_by_xpath(self.popularPreGameX[i]).get_attribute("innerHTML")
                        dataList.append(data)
                    except NoSuchElementException:
                        dataList.append("NA")

        # Utilizing a custom created package in order to retrieve the correct gameID for this specific game
        gameID = matchups.gettingGameID(cursor, dataList[6], dataList[0], str(date.today()))

        # adding the data into their appropriate database tables

        # This is the spread data that needs to be inserted
        sql = "INSERT INTO spreads (team, gameID, FDspread, FDspreadodds) VALUES (%s, %s, %s, %s)"
        val = (dataList[0], gameID, dataList[1], dataList[2])
        cursor.execute(sql, val)
        db.commit()

        sql = "INSERT INTO spreads (team, gameID, FDspread, FDspreadodds) VALUES (%s, %s, %s, %s)"
        val = (dataList[6], gameID, dataList[7], dataList[8])
        cursor.execute(sql, val)
        db.commit()

        # Inserting the moneyline data for the teams
        sql = "INSERT INTO moneyline (gameID, homeTeamMoney, awayTeamMoney) VALUES (%s, %s, %s)"
        val = (gameID, dataList[9], dataList[3])
        cursor.execute(sql, val)
        db.commit()

        # Inserting into the overunder table
        sql = "INSERT INTO overunder (gameID, fdOver, fdOverOdds, fdUnder, fdUnderOdds) VALUES (%s, %s, %s, %s, %s)"
        val = (gameID, dataList[4], dataList[5], dataList[10], dataList[11])
        cursor.execute(sql, val)


# def main():
#     start = datetime.now()
#     options = webdriver.ChromeOptions()
#     options.add_argument("--auto-open-devtools-for-tabs")
#     # after being tested - headless browser proves to be 2x the speed of non headeless browser
#     options.headless = True
#     driver = webdriver.Chrome("C:/ProjectV2/venv/Scripts/chromedriver.exe", options=options)
#
#     # getting the list of basketball game url's and adding them to csv file to be accessed by functions
#     urlList = databaseRet.gettingURL(db, mycursor)
#
#
#
#
#     page = FanDuel(driver)
#     for i in range(len(urlList)):
#         popularPages = page.popular(urlList[i])
#         #print(popularPages)    # THIS PRINT STATEMENT IS WHAT WIL PRINT THE NONE VALUE
#
#     end = datetime.now()
#
#     totalTime = end - start
#     print("total time: " + str(totalTime))
# if __name__ == "__main__":
#     main()


    # IDEA - SPLITTING THE NUMBER OF URLS INTO DIFFERENT THREADS. NOT JUST ONE WEBSITE TO ANOTHER - BUT INSTEAD A
    # DIFFERENT THREAD FOR HALF URLS ON FANDUEL AND SAME FOR OTHER SITES. THIS WAY IT WOULD BE MUCH FASTER.
    # TOTAL TIME IN HEADLESS BROWSER ON 1/18 IS 48 SECONDS. THERE ARE 9 GAMES. 5.3 SECONDS PER GAME

    



