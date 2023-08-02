from selenium.common.exceptions import NoSuchElementException
from importantInfo import matchups
from datetime import *
from importantInfo import ConvertingsTeamName as convert
from selenium.webdriver.common.by import By
import time


class draftKings():

    def __init__(self):

        # From what I can tell - the xpaths are the same whether the game is live or it is not
        # So for that reason - it is different then the FanDuel Class and file because depending on if the game was live or not
        # that would change the xpath that I would have to use - it also will not require a function to tell me the
        # status of the game - as it does not need to be checked.
        self.xPaths = ["//*[@id='root']/section/section[2]/section/section/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[1]/th/a/div/div/div/span/div", # Away Team Name
                       "//*[@id='root']/section/section[2]/section/section/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[1]/td[1]/div/div/div/div[1]/span", # Away Team Spread
                       "//*[@id='root']/section/section[2]/section/section/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[1]/td[1]/div/div/div/div[2]/div[2]/span", # Away Team Spread Odds
                       "//*[@id='root']/section/section[2]/section/section/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[1]/td[3]/div/div/div/div/div[2]/span", # Away Team Moneyline
                       "//*[@id='root']/section/section[2]/section/section/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/div/div/div/div[1]/span[3]", # Over
                       "//*[@id='root']/section/section[2]/section/section/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/div/div/div/div[2]/div[2]/span", #Over Odds
                       "//*[@id='root']/section/section[2]/section/section/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[2]/th/a/div/div/div/span/div", # Home Team Name
                       "//*[@id='root']/section/section[2]/section/section/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[2]/td[1]/div/div/div/div[1]/span", # Home Team Spread
                       "//*[@id='root']/section/section[2]/section/section/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[2]/td[1]/div/div/div/div[2]/div[2]/span", # Home Team Spread Odds
                       "//*[@id='root']/section/section[2]/section/section/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[2]/td[3]/div/div/div/div/div[2]/span", # Home Team Moneyline
                       "//*[@id='root']/section/section[2]/section/section/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[2]/td[2]/div/div/div/div[1]/span[3]", # Under
                       "//*[@id='root']/section/section[2]/section/section/div/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr[2]/td[2]/div/div/div/div[2]/div[2]/span"] # Under Odds


    def popularMarkets(self, url, driver, db):

        cursor = db.cursor()

        driver.get(url)

        dataList = []


        for i in range(len(self.xPaths)):
            try:
                data = driver.find_element(By.XPATH, self.xPaths[i]).get_attribute("innerHTML")
                dataList.append(data)
            except NoSuchElementException:
                dataList.append("NA")

        # The away and home team neames are stored at both of these locations in 'datalist'. But they are scraped
        # from the website in a different form than I want to store it. In order to get the right comparisons, it is
        # important for the team names to be stored in the same exact format. So the team names that are gathered gets
        # converted to the correct format with the following statements:
        dataList[6] = convert.nameConverter(dataList[6])
        dataList[0] = convert.nameConverter(dataList[0])

        gameID = matchups.gettingGameID(cursor, dataList[6], dataList[0], str(date.today()))

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)

        print("gameID is " + str(gameID))

        # This is the spread data that needs to be inserted
        sql = "INSERT INTO spreads (team, gameID, DKspread, DKspreadodds, timeTaken) VALUES (%s, %s, %s, %s, %s)"
        val = (dataList[0], gameID, dataList[1], dataList[2], datetime.today())
        cursor.execute(sql, val)
        db.commit()

        sql = "INSERT INTO spreads (team, gameID, DKspread, DKspreadodds, timeTaken) VALUES (%s, %s, %s, %s, %s)"
        val = (dataList[6], gameID, dataList[7], dataList[8], datetime.today()) #was datetime.now
        cursor.execute(sql, val)
        db.commit()

        # Inserting the moneyline data for the teams
        sql = "INSERT INTO moneyline (gameID, dkHomeTeamMoney, dkAwayTeamMoney, timeTaken) VALUES (%s, %s, %s, %s)"
        val = (gameID, dataList[9], dataList[3], datetime.today())
        cursor.execute(sql, val)
        db.commit()

        # Inserting into the overunder table
        sql = "INSERT INTO overunder (gameID, dkOver, dkOverOdds, dkUnder, dkUnderOdds, timeTaken) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (gameID, dataList[4], dataList[5], dataList[10], dataList[11], datetime.today())
        cursor.execute(sql, val)
        db.commit()

        driver.close()
        print("inserted the data")


    def popularMarkets2(self, driver, db):

        cursor = db.cursor()


        dataList = []


        for i in range(len(self.xPaths)):
            try:
                data = driver.find_element(By.XPATH, self.xPaths[i]).get_attribute("innerHTML")
                dataList.append(data)
            except NoSuchElementException:
                dataList.append("NA")

        # The away and home team neames are stored at both of these locations in 'datalist'. But they are scraped
        # from the website in a different form than I want to store it. In order to get the right comparisons, it is
        # important for the team names to be stored in the same exact format. So the team names that are gathered gets
        # converted to the correct format with the following statements:
        dataList[6] = convert.nameConverter(dataList[6])
        dataList[0] = convert.nameConverter(dataList[0])

        gameID = matchups.gettingGameID(cursor, dataList[6], dataList[0], str(date.today()))

        print("gameID is " + str(gameID))

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)

        # This is the spread data that needs to be inserted
        sql = "INSERT INTO spreads (team, gameID, DKspread, DKspreadodds, timeTaken) VALUES (%s, %s, %s, %s, %s)"
        val = (dataList[0], gameID, dataList[1], dataList[2], datetime.now())
        cursor.execute(sql, val)
        db.commit()

        sql = "INSERT INTO spreads (team, gameID, DKspread, DKspreadodds, timeTaken) VALUES (%s, %s, %s, %s, %s)"
        val = (dataList[6], gameID, dataList[7], dataList[8], datetime.now())
        cursor.execute(sql, val)
        db.commit()

        # Inserting the moneyline data for the teams
        sql = "INSERT INTO moneyline (gameID, dkHomeTeamMoney, dkAwayTeamMoney, timeTaken) VALUES (%s, %s, %s, %s)"
        val = (gameID, dataList[9], dataList[3], datetime.now())
        cursor.execute(sql, val)
        db.commit()

        # Inserting into the overunder table
        sql = "INSERT INTO overunder (gameID, dkOver, dkOverOdds, dkUnder, dkUnderOdds, timeTaken) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (gameID, dataList[4], dataList[5], dataList[10], dataList[11], datetime.now())
        cursor.execute(sql, val)
        db.commit()

        print("inserted the data")