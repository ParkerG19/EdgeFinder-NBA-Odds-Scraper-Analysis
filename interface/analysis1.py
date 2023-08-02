import sys
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np



"""
This performs analysis on a game with teh passed in gameID value. 
It will plot 4 different line charts given the data that is found
from the queries of the database tables. 
These charts will open on a different page when implemented in the GUI
"""
def analysis(gameID):

        # Connect to the database and create a cursor
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Gocubsgo19!!!",
            database="oddsDB"
        )

        mycursor = db.cursor()

        # This query will get the distinct team names for games with given gameID
        query = "SELECT DISTINCT team FROM spreads WHERE gameID = %s"
        vals = (gameID,)
        mycursor.execute(query, vals)
        teams = mycursor.fetchall()

        team1 = teams[0][0]
        team2 = teams[1][0]

        # This query will get the fanduel spread for the first team
        query = "SELECT CAST(FDSpread AS DECIMAL) AS FDSpread, timetaken FROM spreads WHERE gameID = %s AND team = %s AND FDSpread IS NOT NULL AND timetaken IS NOT NULL ORDER BY timetaken"
        vals = (gameID, team1)
        mycursor.execute(query, vals)
        team1FDSpread = mycursor.fetchall()
        df = pd.DataFrame(team1FDSpread, columns=['timetaken', 'FDSpread'])
        print(df)

        # This query will get the fanduel spread for the second team
        query = "SELECT CAST(FDSpread AS DECIMAL) AS FDSpread, timetaken FROM spreads WHERE gameID = %s AND team = %s AND FDSpread IS NOT NULL AND timetaken IS NOT NULL ORDER BY timetaken"
        vals = (gameID, team2)
        mycursor.execute(query, vals)
        team2FDSpread = mycursor.fetchall()
        df2 = pd.DataFrame(team2FDSpread, columns=['timetaken', 'FDSpread'])

        # This query will get teh draftkings spread for the first team
        querydk = "SELECT CAST(DKSpread AS DECIMAL) AS DKSpread, timetaken FROM spreads WHERE gameID = %s AND team = %s AND DKSpread IS NOT NULL AND timetaken IS NOT NULL ORDER BY timetaken"
        vals = (gameID, team1)
        mycursor.execute(querydk, vals)
        team1DKSpread = mycursor.fetchall()
        df3 = pd.DataFrame(team1DKSpread, columns=['timetaken', 'DKSpread'])

        querydk = "SELECT CAST(DKSpread AS DECIMAL) AS DKSpread, timetaken FROM spreads WHERE gameID = %s AND team = %s AND DKSpread IS NOT NULL AND timetaken IS NOT NULL ORDER BY timetaken"
        vals = (gameID, team2)
        mycursor.execute(querydk, vals)
        team2DKSpread = mycursor.fetchall()
        df4 = pd.DataFrame(team2DKSpread, columns=['timetaken', 'DKSpread'])

        #------------------------------------------------------------------------------------#
        # Now will be doing queries and analysis based off of the moneyline data

        # This will get the moneyline info for both teams as given on FanDuel
        queryfd1 = "SELECT homeTeamMoney, timeTaken FROM moneyline WHERE gameID = %s AND (dkHomeTeamMoney IS NULL AND dkAwayTeamMoney IS NULL) ORDER BY timeTaken, CAST(homeTeamMoney AS SIGNED)"
        vals = (gameID,)
        mycursor.execute(queryfd1, vals)
        fanduelMoney= mycursor.fetchall()
        df5 = pd.DataFrame(fanduelMoney, columns=['homeTeamMoney', 'timetaken'])


        queryfd2 = "SELECT awayTeamMoney, timeTaken FROM moneyline WHERE gameID = %s AND (dkHomeTeamMoney IS NULL AND dkAwayTeamMoney IS NULL) ORDER BY timeTaken, CAST(awayTeamMoney AS SIGNED)"
        vals = (gameID,)
        mycursor.execute(queryfd2, vals)
        fanduelMoney= mycursor.fetchall()
        df6 = pd.DataFrame(fanduelMoney, columns=['awayTeamMoney', 'timetaken'])

        # This will get the moneyline info for both teams as given on Draftkings

        queryMoneyDk1 = "SELECT dkHomeTeamMoney, timeTaken FROM moneyline WHERE gameID = %s AND (homeTeamMoney IS NULL AND awayTeamMoney IS NULL) ORDER BY timeTaken, CAST(dkHomeTeamMoney AS SIGNED)"
        vals = (gameID,)
        mycursor.execute(queryMoneyDk1, vals)
        dkMoney = mycursor.fetchall()
        df7 = pd.DataFrame(dkMoney, columns=['dkHomeTeamMoney', 'timetaken'])


        queryMoneyDk2 = "SELECT dkAwayTeamMoney, timeTaken FROM moneyline WHERE gameID = %s AND (homeTeamMoney IS NULL AND awayTeamMoney IS NULL) ORDER BY timeTaken, CAST(dkAwayTeamMoney AS SIGNED)"
        vals = (gameID,)
        mycursor.execute(queryMoneyDk2, vals)
        dkMoney = mycursor.fetchall()
        df8 = pd.DataFrame(dkMoney, columns=['dkAwayTeamMoney', 'timetaken'])

        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 6))  # create figure with two subplots

        # plot data on first subplot - this will be for the spread data
        print(df)

        ax1.plot(df['FDSpread'], df['timetaken'], label='FDSpread')
        ax1.plot(df3['DKSpread'], df3['timetaken'],label='DKSpread')
        ax1.legend(loc='best')
        ax1.set_title('Spread over Time')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Spread for ' + team1, fontsize=8)
        ax1.tick_params(axis='x', rotation=90, labelsize=6)

        # plot data on second subplot
        ax2.plot(df2['FDSpread'], df2['timetaken'], label='FDSpread')
        ax2.plot(df4['DKSpread'], df4['timetaken'],label='DKSpread')
        ax2.legend(loc='best')
        ax2.set_title('Spread over Time')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Spread for ' + team2, fontsize=8)
        ax2.tick_params(axis='x', rotation=90, labelsize=6)

        #-----------------------------------------------------------------------#
        # These will be the plots for the moneyline data

        # The first plot will be for the home team
        ax4.plot(df5['timetaken'],df5['homeTeamMoney'], label = 'Fanduel')
        ax4.plot(df7['timetaken'],df7['dkHomeTeamMoney'], label = 'DraftKings')
        ax4.legend(loc='best')
        ax4.set_title('Moneyline over time')
        ax4.set_xlabel('Time')
        ax4.set_ylabel('Moneyline for ' + team2, fontsize=8)
        ax4.tick_params(axis='x', rotation=90,labelsize=6)

        # The second plot will be for the away team
        ax3.plot(df6['timetaken'], df6['awayTeamMoney'], label = 'Fanduel')
        ax3.plot(df8['timetaken'], df8['dkAwayTeamMoney'], label = 'DraftKings')
        ax3.legend(loc='best')
        ax3.set_title('Moneyline over time')
        ax3.set_xlabel('Time')
        ax3.set_ylabel('Moneyline for ' + team1, fontsize=8)
        ax3.tick_params(axis='x', rotation=90,labelsize=6)

        # adjust spacing between subplots and show the chart
        plt.subplots_adjust(wspace=0.5, hspace=0.5)
        plt.show()



# if __name__ == '__main__':
#     analysis(24772)