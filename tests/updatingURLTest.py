from importantInfo import matchups
from selenium import webdriver
import mysql.connector
import Basketball.FanDuel as fd
import time as t
from selenium.webdriver.common.by import By
from datetime import *
from importantInfo import updatingURL as upd


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Gocubsgo19!!!",
    database="oddsDB"
)

mycursor = db.cursor()
#
options = webdriver.ChromeOptions()
options.add_argument("--auto-open-devtools-for-tabs")
# setting the window size allows interaction with the web page when it is in headless mode
options.add_argument('--window-size=1920,1080')
# after being tested - headless browser proves to be 2x the speed of non headeless browser
#options.headless = True
driver = webdriver.Chrome("C:/ProjectV2/venv/Scripts/chromedriver.exe", options=options)



#   THESE ARE THE THINGS THAT NEED TO BE RUN AT THE SAME TIME AND ON SOME SORT OF SCHEDULE
upd.updateURLdk(mycursor, driver, db)
upd.updateURL(mycursor, driver, db)

"""
Checking to make sure that the gettingMatchupURL is working for the draftkings function version
"""
driver.close()
# options = webdriver.ChromeOptions()
# options.add_argument("--auto-open-devtools-for-tabs")
# # setting the window size allows interaction with the web page when it is in headless mode
# options.add_argument('--window-size=1920,1080')
#
#
# driver = webdriver.Chrome("C:/ProjectV2/venv/Scripts/chromedriver.exe",options=options)
# upd.gettingMatchupURLdk(driver, mycursor)




