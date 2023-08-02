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
import time
import random


start = datetime.now()


def makingDrivers():
    options = webdriver.ChromeOptions()
    options.add_argument("--auto-open-devtools-for-tabs")

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


"""
Establishing database connection - needs to be updated with credentials
"""
def databaseConn():

    db = mysql.connector.connect(
        host="YOUR_HOST",
        user="YOUR_USER",
        passwd="YOUR_PASSWORD",
        database="YOUR_DB_NAME"
    )

    mycursor = db.cursor()

    return db


connection = databaseConn()
db = connection


# getting all of the URL's available for today and later by calling databaseRet
# 'allURLS' will be the entire list of URLs, both fanduel and draftkings
urlList = databaseRet.gettingURLfd(db, db.cursor())
urlList2 = databaseRet.gettingURLdk(db, db.cursor())
allURLS = urlList + urlList2

draftKingsString = "https://sportsbook.draftkings.com"
fanduelString = "https://sportsbook.fanduel.com"

threads = []
fd = FanDuel.FanDuel()
dk = DraftKings.draftKings()

# Loop will run until the program is ended
while True:
    # Loop through every URL in the list
    for urls in allURLS:

        print("Making thread")
        # Creating a new driver instance and a new database connection
        driver = makingDrivers()
        db = databaseConn()

        # This is used to work with the fanduel
        # fanduelString is previously defined, and will always be the same, this is
        # how the program can differentiate which URL is being used
        if fanduelString in urls:
            thread1 = threading.Thread(target=fd.popular, args=(urls, driver, db))
        # This is used to work with the draftkings
        # If it was not a fanduelString then it will be a draftKings string, and will execute the
        # draftkings script to scrape the data
        else:
            thread1 = threading.Thread(target=dk.popularMarkets, args=(urls, driver, db))

        threads.append(thread1)  # append the thread to the list of threads
        thread1.start()   # Start the thread

    # Waits for all of the threads to be done to stop executing
    for t in threads:
        t.join()

    # sleeping for 30 seconds
    print("sleeping for 30 seconds")
    time.sleep(30)




end = datetime.now()

totalTime = end - start
print("total time: " + str(totalTime))
