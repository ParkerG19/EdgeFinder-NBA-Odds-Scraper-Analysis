import mysql.connector



db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Gocubsgo19!!!",
    database="oddsDB"
)


mycursor = db.cursor()

mycursor.execute('TRUNCATE spreads')
