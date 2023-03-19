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

start = datetime.now()



def makingDrivers():
    options = webdriver.ChromeOptions()
    options.add_argument("--auto-open-devtools-for-tabs")
    #options.headless = True

    driver = webdriver.Chrome("C:/ProjectV2/venv/Scripts/chromedriver.exe", options=options)

    return driver


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

# Getting the URLS from the database for games on Fanduel
urlList1 = databaseRet.gettingURLfd(db, db.cursor())

# Getting the URLS from the database for games on DraftKings
urlList2 = databaseRet.gettingURLdk(db, db.cursor())


allURLS = urlList1 + urlList2


threads = []
fd = FanDuel.FanDuel()
dk = DraftKings.draftKings()

draftKingsString = "https://sportsbook.draftkings.com"
fanduelString = "https://sportsbook.fanduel.com"

# for urls in allURLS:
#
#     driver = makingDrivers()
#     db = databaseConn()
#
#     # This is for calling the draft kings package
#     if draftKingsString in urls:
#         thread = threading.Thread(target=dk.popularMarkets(urls, driver, db))
#         threads.append(thread)
#     else:
#         thread = threading.Thread(target=fd.popular, args=(urls, driver, db))
#         threads.append(thread)
#

loops = 4 * round(len(allURLS) / 4) # This is how many times I need to go back into the list of URLS
                                    # It is rounded to 4 because that is how many threads I have - and I want to cover
                                    # every URL that is in the list - this makes sure that none will get skipped

# This will loop through the threads four at a time to optimal exececution on my system - threads are coming
# from the list that was previously generated in the last bunch of code.

for i in range (0, loops, 3):

    cycles = []

    if allURLS[i] in draftKingsString:
        try:
            driver1 = makingDrivers()
            thread1 = threading.Thread(target=dk.popularMarkets(allURLS[i], driver1, db))
            threads.append(thread1)
            thread1.start()
        except IndexError:
            break

        try:
            driver2 = makingDrivers()
            thread2 = threading.Thread(target=dk.popularMarkets(allURLS[i+1], driver2, db))
            threads.append(thread2)
            thread2.start()
        except IndexError:
            break

        try:
            driver3 = makingDrivers()
            thread3 = threading.Thread(target=dk.popularMarkets(allURLS[i+2], driver3, db))
            threads.append(thread3)
            thread3.start()
        except IndexError:
            break

        try:
            driver4 = makingDrivers()
            thread4 = threading.Thread(target=dk.popularMarkets(allURLS[i+3], driver4, db))
            threads.append(thread4)
            thread4.start()

        except IndexError:
            break


    else:
        try:
            driver1 = makingDrivers()
            thread1 = threading.Thread(target=dk.popularMarkets(allURLS[i], driver1, db))
            threads.append(thread1)
            thread1.start()

            driver2 = makingDrivers()
            thread2 = threading.Thread(target=dk.popularMarkets(allURLS[i+1], driver2, db))
            threads.append(thread2)
            thread2.start()

            driver3 = makingDrivers()
            thread3 = threading.Thread(target=dk.popularMarkets(allURLS[i+2], driver3, db))
            threads.append(thread3)
            thread3.start()

            driver4 = makingDrivers()
            thread4 = threading.Thread(target=dk.popularMarkets(allURLS[i+3], driver4, db))
            threads.append(thread4)
            thread4.start()
        except IndexError:
            break

        # try:
        #     driver2 = makingDrivers()
        #     thread2 = threading.Thread(target=dk.popularMarkets(allURLS[i+1], driver2, db))
        #     threads.append(thread2)
        #     thread2.start()
        # except IndexError:
        #     break
        #
        # try:
        #     driver3 = makingDrivers()
        #     thread3 = threading.Thread(target=dk.popularMarkets(allURLS[i+2], driver3, db))
        #     threads.append(thread3)
        #     thread3.start()
        # except IndexError:
        #     break
        #
        # try:
        #     driver4 = makingDrivers()
        #     thread4 = threading.Thread(target=dk.popularMarkets(allURLS[i+3], driver4, db))
        #     threads.append(thread4)
        #     thread4.start()
        # except IndexError:
        #     break


    # Unsure of what this exactly will do and if it is needed in this location - I think that it waits for all the threads to finish
    # and then the next iteration of the loop should run
    for t in threads:
        t.join()




# for urls in urlList:
#     print("Making thread")
#     driver = makingDrivers()
#     db = databaseConn()
#     # This is used to work with the fanduel - testing purposes are only testing one website at a time
#     #thread1 = threading.Thread(target=fd.popular, args=(urls, driver, db))
#
#     # This is used to work with teh draftkings = testing purposes are only testing one website at a time
#     thread1 = threading.Thread(target=dk.popularMarkets(urls, driver, db))
#
#     threads.append(thread1)
#     thread1.start()


# for t in threads:
#     t.join()



end = datetime.now()

totalTime = end - start
print("total time: " + str(totalTime))
