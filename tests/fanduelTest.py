from Basketball import FanDuel
from selenium import webdriver
import mysql.connector
from importantInfo import matchups
from importantInfo import databaseRet
import threading
from datetime import *

start = datetime.now()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Gocubsgo19!!!",
    database="oddsDB"
)

mycursor = db.cursor()


options = webdriver.ChromeOptions()
options.add_argument("--auto-open-devtools-for-tabs")
# after being tested - headless browser proves to be 2x the speed of non headeless browser
#options.headless = True
driver = webdriver.Chrome("C:/ProjectV2/venv/Scripts/chromedriver.exe", options=options)

fd = FanDuel.FanDuel(driver)
fd1 = FanDuel.FanDuel(driver)
urlList = databaseRet.gettingURL(db, mycursor)

#page = FanDuel(driver)
for i in range(len(urlList)):
    #popularPages = fd.popular(urlList[i])
    # print(popularPages)    # THIS PRINT STATEMENT IS WHAT WIL PRINT THE NONE VALUE


    t1 = threading.Thread(target=fd.popular, args=(urlList[i],))
    t1.start()
    t1.join()

end = datetime.now()

totalTime = end - start
print("total time: " + str(totalTime))