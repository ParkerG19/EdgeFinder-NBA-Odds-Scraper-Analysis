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
print(start)
def makingDrivers():
    options = webdriver.ChromeOptions()
    options.add_argument("--auto-open-devtools-for-tabs")
    options.headless = True

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




loops = 4 * round((len(allURLS) + 4) / 4) # This is how many times I need to go back into the list of URLS
                                    # It is rounded to 4 because that is how many threads I have - and I want to cover
                                    # every URL that is in the list - this makes sure that none will get skipped




"""
This is in need of some sort of redundancy. Because of the format of 'loops'
the loop will most likely look for an index that will be out of bounds. Because
loops will go up to all multiples of 4 and this will only work out specifically in 
rare cases. Until this is fixed, I will most likely continue to get a 
'list index out of range error' towards the backend of the program finishing. Overall, I think that 
this version is slower anyway. So if I ever come back to this program - that is what needs to be fixed
"""

for i in range(0,loops + 4, 4):
    threads = []

    if fanduelString in allURLS[i]:
        print("Fanduel")

        db = databaseConn()
        driver1 = makingDrivers()
        thread1 = threading.Thread(target=fd.popular, args = (allURLS[i], driver1, db))
        threads.append(thread1)
        thread1.start()
    else:
        db11 = databaseConn()

        driver1 = makingDrivers()
        thread1 = threading.Thread(target=dk.popularMarkets, args = (allURLS[i], driver1, db11))
        threads.append(thread1)
        thread1.start()

    if fanduelString in allURLS[i+1]:
        print("Fanduel")

        db2 = databaseConn()
        driver2 = makingDrivers()
        thread2 = threading.Thread(target=fd.popular, args = (allURLS[i + 1], driver2, db2))
        threads.append(thread2)
        thread2.start()
    else:
        db22 = databaseConn()
        driver2 = makingDrivers()
        thread2 = threading.Thread(target=dk.popularMarkets, args = (allURLS[i + 1], driver2, db22))
        threads.append(thread2)
        thread2.start()

    if fanduelString in allURLS[i+2]:
        print("Fanduel")

        db3 = databaseConn()
        driver3 = makingDrivers()
        thread3 = threading.Thread(target=fd.popular, args = (allURLS[i + 2], driver3, db3))
        threads.append(thread3)
        thread3.start()
    else:
        db33 = databaseConn()
        driver3 = makingDrivers()
        thread3 = threading.Thread(target=dk.popularMarkets, args = (allURLS[i + 2], driver3, db33))
        threads.append(thread3)
        thread3.start()

    if fanduelString in allURLS[i+3]:
        print("Fanduel")
        db4 = databaseConn()
        driver4 = makingDrivers()
        thread4 = threading.Thread(target=fd.popular, args = (allURLS[i + 3], driver4, db4))
        threads.append(thread4)
        thread4.start()
    else:
        db44 = databaseConn()
        driver4 = makingDrivers()
        thread4 = threading.Thread(target=dk.popularMarkets, args = (allURLS[i + 3], driver4, db44))
        threads.append(thread4)
        thread4.start()

    for t in threads:
        t.join()



end = datetime.now()

totalTime = end - start
print("total time: " + str(totalTime))
