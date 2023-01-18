from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from random import randint
from selenium.common.exceptions import NoSuchElementException
from importantInfo import databaseRet
import mysql.connector







db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Gocubsgo19!!!",
    database="oddsDB"
)

mycursor = db.cursor()



list = databaseRet.gettingURL(db, mycursor)

print(list[len(list) - 1])


