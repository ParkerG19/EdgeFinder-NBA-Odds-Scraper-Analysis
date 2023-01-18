import mysql.connector



db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Gocubsgo19!!!",
    database="oddsDB"
)


mycursor = db.cursor()

mycursor.execute("CREATE TABLE matchups (gameID INT, date DATE, time VARCHAR(255),awayTeam VARCHAR(255),homeTeam VARCHAR(255))")

