from Basketball import FanDuel
from Basketball import DraftKings
from selenium import webdriver
import mysql.connector
from importantInfo import matchups
from importantInfo import databaseRet
import threading
from datetime import *
import concurrent.futures
from concurrent.futures import wait
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time as t
import random


start = datetime.now()

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="Gocubsgo19!!!",
#     database="oddsDB"
# )
#
# mycursor = db.cursor()


# options = webdriver.ChromeOptions()
# options.add_argument("--auto-open-devtools-for-tabs")
# # after being tested - headless browser proves to be 2x the speed of non headeless browser
# options.headless = True
# driver = webdriver.Chrome("C:/ProjectV2/venv/Scripts/chromedriver.exe", options=options)

#fd1 = FanDuel.FanDuel(driver)

#page = FanDuel(driver)
    #popularPages = fd.popular(urlList[i])
    # print(popularPages)    # THIS PRINT STATEMENT IS WHAT WIL PRINT THE NONE VALUE
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
#     executor.map(fd.popular, urlList)







def makingDrivers():
    options = webdriver.ChromeOptions()
    options.add_argument("--auto-open-devtools-for-tabs")
    # options.headless = True

    options.add_argument("--headless=new")
    options.add_argument("--window-size=974,1040")

    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    # Adding argument to disable the AutomationControlled flag
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Exclude the collection of enable-automation switches
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Turn-off userAutomationExtension 
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome("C:/ProjectV2/venv/Scripts/chromedriver.exe", options=options)

    return driver


#fd = FanDuel.FanDuel(makingDrivers())


# def popular(url,driver):
#
#     driver.get(url)
#     # This should open the inspector page - which I think needs to happen in order to load the elements that are
#     # on the page - because the page is dynamic. I am not seeing the inspector open - but it doesn't seem like it
#     # has to on this computer - it may have to on my laptop becuase that is where I learned that this was a solution
#     # to not being able to find the elements that are on the page
#
#     # Don't want to use all of the try loops if I don't have to. I can append to a list and make a dataframe from that information
#     isItLive = fd.live(driver)
#
#     # dataList will contain all of the information that is gathered from the 'popular' page including the
#     # team name, spread, spread odds, moneyline, over, over odds,..... etc - and in that order; starting with the away team
#     dataList = []
#
#     # TESTING PURPOSES
#     # print(isItLive)
#
#     # Checking to see if the game is live - as that will determine the xpath that I am using
#     # After checking to see if it is live - trys to find element and appends to list if it is found
#     # if the element cannot be found - that means that the bet is not available - a "NA" value will be appended
#     # to the list as that is the value that is put into the database
#     if (isItLive == 1):
#
#         for i in range(len(fd.popularLiveX)):
#             try:
#                 data = driver.find_element_by_xpath(fd.popularLiveX[i]).get_attribute("innerHTML")
#                 dataList.append(data)
#             except NoSuchElementException:
#                 dataList.append("NA")
#
#     else:
#         for i in range(len(fd.popularPreGameX)):
#             try:
#                 data = driver.find_element_by_xpath(fd.popularPreGameX[i]).get_attribute("innerHTML")
#                 dataList.append(data)
#             except NoSuchElementException:
#                 dataList.append("NA")
#
#     # Utilizing a custom created package in order to retrieve the correct gameID for this specific game
#     gameID = matchups.gettingGameID(mycursor, dataList[6], dataList[0], str(date.today()))
#
#     # adding the data into their appropriate database tables
#
#     # This is the spread data that needs to be inserted
#     sql = "INSERT INTO spreads (team, gameID, FDspread, FDspreadodds) VALUES (%s, %s, %s, %s)"
#     val = (dataList[0], gameID, dataList[1], dataList[2])
#     mycursor.execute(sql, val)
#     db.commit()
#
#     sql = "INSERT INTO spreads (team, gameID, FDspread, FDspreadodds) VALUES (%s, %s, %s, %s)"
#     val = (dataList[6], gameID, dataList[7], dataList[8])
#     mycursor.execute(sql, val)
#     db.commit()
#
#     # Inserting the moneyline data for the teams
#     sql = "INSERT INTO moneyline (gameID, homeTeamMoney, awayTeamMoney) VALUES (%s, %s, %s)"
#     val = (gameID, dataList[9], dataList[3])
#     mycursor.execute(sql, val)
#     db.commit()
#
#     # Inserting into the overunder table
#     sql = "INSERT INTO overunder (gameID, fdOver, fdOverOdds, fdUnder, fdUnderOdds) VALUES (%s, %s, %s, %s, %s)"
#     val = (gameID, dataList[4], dataList[5], dataList[10], dataList[11])
#     mycursor.execute(sql, val)


def databaseConn():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Gocubsgo19!!!",
        database="oddsDB"
    )

    mycursor = db.cursor()

    return db


connection = databaseConn()
db = connection


urlList = databaseRet.gettingURLfd(db, db.cursor())
urlList2 = databaseRet.gettingURLdk(db, db.cursor())

allURLS = urlList + urlList2



draftKingsString = "https://sportsbook.draftkings.com"
fanduelString = "https://sportsbook.fanduel.com"

threads = []
fd = FanDuel.FanDuel()
dk = DraftKings.draftKings()

for urls in allURLS:

    # I used this random to imitate more a human - it slows down the program - unsure at this point if it is necessary
    randomNum = random.randint(1,8)
    t.sleep(randomNum)

    print("Making thread")
    driver = makingDrivers()
    db = databaseConn()
    # This is used to work with the fanduel - testing purposes are only testing one website at a time
    if fanduelString in urls:
        t.sleep(randomNum)
        thread1 = threading.Thread(target=fd.popular, args=(urls, driver, db))
    # This is used to work with teh draftkings = testing purposes are only testing one website at a time
    else:
        thread1 = threading.Thread(target=dk.popularMarkets, args= (urls, driver, db))

    threads.append(thread1)
    thread1.start()


for t in threads:
    t.join()



end = datetime.now()

totalTime = end - start
print("total time: " + str(totalTime))
