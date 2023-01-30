from datetime import *
import re

def timeConverter():
    today = date.today()
    # setting it equal to today's date values
    day = str(today.day)
    month = today.month
    year = str(today.year)

    if (month==1):
        newMonth="Jan"
    elif (month==2):
        newMonth="Feb"
    elif (month==3):
        newMonth="Mar"
    elif (month==4):
        newMonth="Apr"
    elif (month==5):
        newMonth="May"
    elif (month==6):
        newMonth="Jun"
    elif (month==7):
        newMonth="Jul"
    elif (month==8):
        newMonth="Aug"
    elif (month==9):
        newMonth="Sep"
    elif (month==10):
        newMonth="Oct"
    elif (month==11):
        newMonth="Nov"
    else:
        newMonth="Dec"

    partialDate = newMonth + " " + day + ", " + year

    return partialDate


def timeConverter2(date):
    newDate = re.sub(",","",date)
    newDate = newDate.split()
    print(newDate)

    month = newDate[1]
    day = newDate[2]
    year = newDate[3]

    if (month=="Jan"):
        newMonth = "01"
    elif (month=="Feb"):
        newMonth = "02"
    elif (month=="Mar"):
        newMonth = "03"
    elif (month=="Apr"):
        newMonth = "04"
    elif (month=="May"):
        newMonth = "05"
    elif (month=="Jun"):
        newMonth = "06"
    elif (month=="Jul"):
        newMonth = "07"
    elif (month=="Aug"):
        newMonth = "08"
    elif (month=="Sep"):
        newMonth = "09"
    elif (month=="Oct"):
        newMonth = "10"
    elif (month=="Nov"):
        newMonth = "11"
    else:
        newMonth = "12"

    newDate = year + '-' + newMonth + '-' + day
    return newDate


