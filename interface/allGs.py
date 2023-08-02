# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'redoAllGames.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtGui import QPixmap
from interface import analysis1 #howItWorks

from openPages import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from interface import displayingData as data
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QToolBar, QLineEdit, QAction
from PyQt5.QtGui import QColor, QCursor
from PyQt5.QtCore import Qt, QSize
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QToolBar,QSizePolicy
from PyQt5.QtGui import QColor, QCursor
from PyQt5.QtCore import Qt, QSize

class allGames(object):
    #
    # def openHome(self):
    #
    #
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = homePage()
    #     self.ui.setupUi(self.window)
    #
    #     self.MainWindow.hide()
    #     self.window.showMaximized()
    #     self.window.show()
    #
    # def openLive(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = allGames()
    #     self.ui.setupUi(self.window)
    #     self.MainWindow.hide()
    #     self.window.showMaximized()
    #     self.window.show()
    #
    # def openHow(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = howItWorks()
    #     self.ui.setupUi(self.window)
    #     self.MainWindow.hide()
    #     self.window.showMaximized()
    #     self.window.show()

    def getSearchTerm(self):
        # Get the search term entered by the user
        search_term = self.search_edit.text()

        # Do something with the search term
        self.openAnalysis(search_term)
    def openAnalysis(self, gameID):
        analysis1.analysis(gameID)
        # self.analysisWindow = analysis.analysis(gameID)
        # self.analysisWindow.showMaximized()
        # self.analysisWindow.show()


    def setupUi(self, MainWindow):
        #Adding the menu at the top of the screen:


        # WANT TO HAVE A FUNCTION THAT CAN BE CALLED AND GIVE THE NUMBER OF GAMES THAT ARE AVAILABLE AT THE MOMENET
        # STARTED WORKING ON THE FUNCTION BUT NEED MORE DETAIL ON THE DATABASE IN ORDER TO GET THE RIGHT RESULTS.
        numberOfGames = len(data.getGameID())

        _translate = QtCore.QCoreApplication.translate

        # Adding the menu at the top of the screen:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.showMaximized()
        MainWindow.setStyleSheet("background-color: black;")

        self.MainWindow = MainWindow
        # Set up the UI for the rest of the page
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("background-color: #1c1c1c;")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 773, 1012))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.bottomFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)

        # Need to set the minimum size to be based off of the number of games - this will allow there to be scroll.
        # Each game takes up 91 pixels of the screen - and it starts at 120. I would say the very minimum should be
        # 500 pixels. so that the screen will still look okay no matter the amount of games.
        minSize = 140 + (numberOfGames * 95)
        self.bottomFrame.setMinimumSize(QtCore.QSize(0, minSize))


        self.bottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomFrame.setObjectName("bottomFrame")

        # From here on - this is the stuff that needs to be repeated for the number of games and to change the
        # words that are in the display

        # The data that is going to go in these fields will need to be called directly from the loop and won't have to be
        # passed into the function. Because for each game - it will be different and it will correlate to the iteration
        # of the list of gameID's that is going to be gotten from the numberOFgames.py file.

        startingYofTeams = 125
        startingYofTopTeam = 125
        startingYofBottomTeam = 175
        lineMedianY = 210
        pushButtonStartY = 150
        idLabelStartX = 200
        idLabelStartY = 300

        listOfGameIDs = data.getGameID()



        print(listOfGameIDs)
        for i in range(numberOfGames):
            _translate = QtCore.QCoreApplication.translate

            gameID = listOfGameIDs[i]
            #print(listOfGameIDs[i])
            # These variable are all things that will need to be displayed in their correct location and will need to be gotten
            # based off their gameID's whcih will come from the function call at the beginning of this method.
            #print(gameID)
            homeTeam, awayTeam = data.gettingTeams(gameID)
            HTfdSpread, HTfdSpreadOdds, HTdkSpread, HTdkSpreadOdds = data.gettingSpreadInfo(gameID, homeTeam)
            ATfdSpread, ATfdSpreadOdds, ATdkSpread, ATdkSpreadOdds = data.gettingSpreadInfo(gameID, awayTeam)
            fdHomeMoney, fdAwayMoney, dkHomeMoney, dkAwayMoney = data.gettingMoneyLineInfo(gameID)
            fdOver, fdOverOdds, fdUnder, fdUnderOdds, dkOver, dkOverOdds, dkUnder, dkUnderOdds = data.gettingOverUnder(gameID)
            self.frame_2 = QtWidgets.QFrame(self.bottomFrame)
            self.frame_2.setGeometry(QtCore.QRect(0, startingYofTeams, 181, 106))# ONE MORE CTRL Z
            startingYofTeams += 95
            self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_2.setObjectName("frame_2")
            self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
            self.verticalLayout_3.setObjectName("verticalLayout_3")

            # This created the button that will be able to view the individual game that it is attached to
            # self.pushButton = QtWidgets.QPushButton(self.bottomFrame)
            # #self.pushButton.setProperty("gameID", gameID)
            # self.pushButton.clicked.connect(self.buttonClick)
            # #self.pushButton.clicked.connect(lambda: self.openAnalysis(self.pushButton.property(("gameID"))))
            # #print(self.pushButton.property("gameID"))


            # self.pushButton.setGeometry(QtCore.QRect(206, pushButtonStartY, 83, 48))
            # pushButtonStartY += 95
            # self.pushButton.setObjectName("pushButton")
            # self.pushButton.setText(_translate("MainWindow", "History"))
            # self.pushButton.setStyleSheet("background-color: navy; color: white;")


            self.label = QtWidgets.QLabel(self.frame_2)
            self.label.setObjectName("label")
            self.verticalLayout_3.addWidget(self.label)
            self.label.setText(_translate("MainWindow", awayTeam))
            self.label.setStyleSheet("color: white;")


            self.label_2 = QtWidgets.QLabel(self.frame_2)
            self.label_2.setObjectName("label_2")
            self.verticalLayout_3.addWidget(self.label_2)
            # self.label_2.setText(_translate("MainWindow", "@"))
            # self.label_2.setStyleSheet("color: white;")



            self.label_2.setText(_translate("MainWindow", homeTeam))
            self.label_2.setStyleSheet("color: white;")

            # Adding the gameID for the user to see so that they can search for it
            self.label31 = QtWidgets.QLabel(self.frame_2)
            self.label31.setObjectName("label31")
            self.label31.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self.verticalLayout_3.addWidget(self.label31)
            gameIDString = "GameID: " + str(gameID)
            self.label31.setText(_translate("MainWindow", gameIDString))
            self.label31.setStyleSheet("color: white; font-size: 8px;")

            self.label_3 = QtWidgets.QLabel(self.frame_2)
            self.label_3.setObjectName("label_3")
            self.verticalLayout_3.addWidget(self.label_3)
            # self.label31.move(idLabelStartX, idLabelStartY)
            # idLabelStartX += 95
            # idLabelStartY += 95

            self.frame = QtWidgets.QFrame(self.bottomFrame)
            self.frame.setGeometry(QtCore.QRect(300, startingYofTopTeam, 688, 36))
            startingYofTopTeam += 95
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
            self.horizontalLayout.setObjectName("horizontalLayout")

            # away team spread fanduel
            self.label_9 = QtWidgets.QLabel(self.frame)
            self.label_9.setObjectName("label_9")
            self.horizontalLayout.addWidget(self.label_9)
            self.label_9.setText(_translate("MainWindow", ATfdSpread))
            self.label_9.setStyleSheet("color: white;")


            #away team spread draftkings
            self.label_8 = QtWidgets.QLabel(self.frame)
            self.label_8.setObjectName("label_8")
            self.horizontalLayout.addWidget(self.label_8)
            self.label_8.setText(_translate("MainWindow", ATdkSpread))
            self.label_8.setStyleSheet("color: white;")

            # away team moneyline fanduel
            self.label_7 = QtWidgets.QLabel(self.frame)
            self.label_7.setObjectName("label_7")
            self.horizontalLayout.addWidget(self.label_7)
            self.label_7.setText(_translate("MainWindow", fdAwayMoney))
            self.label_7.setStyleSheet("color: white;")


            # away team moneyline draftkings
            self.label_6 = QtWidgets.QLabel(self.frame)
            self.label_6.setObjectName("label_6")
            self.horizontalLayout.addWidget(self.label_6)
            self.label_6.setText(_translate("MainWindow", dkAwayMoney))
            self.label_6.setStyleSheet("color: white;")


            # fanduel over
            self.label_5 = QtWidgets.QLabel(self.frame)
            self.label_5.setObjectName("label_5")
            self.horizontalLayout.addWidget(self.label_5)
            self.label_5.setText(_translate("MainWindow", fdOver))
            self.label_5.setStyleSheet("color: white;")


            # draftkings over
            self.label_4 = QtWidgets.QLabel(self.frame)
            self.label_4.setObjectName("label_4")
            self.horizontalLayout.addWidget(self.label_4)
            self.label_4.setText(_translate("MainWindow", dkOver ))
            self.label_4.setStyleSheet("color: white;")



            self.frame_3 = QtWidgets.QFrame(self.bottomFrame)
            self.frame_3.setGeometry(QtCore.QRect(300, startingYofBottomTeam, 688, 48))
            startingYofBottomTeam+=95
            self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_3.setObjectName("frame_3")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")

            # Home Team Spread FAnduel
            self.label_10 = QtWidgets.QLabel(self.frame_3)
            self.label_10.setObjectName("label_10")
            self.horizontalLayout_2.addWidget(self.label_10)
            self.label_10.setText(_translate("MainWindow", HTfdSpread))
            self.label_10.setStyleSheet("color: white;")


            # Home TEam spread draftkings
            self.label_11 = QtWidgets.QLabel(self.frame_3)
            self.label_11.setObjectName("label_11")
            self.horizontalLayout_2.addWidget(self.label_11)
            self.label_11.setText(_translate("MainWindow",HTdkSpread ))
            self.label_11.setStyleSheet("color: white;")


            # home team moneyline fanduel
            self.label_12 = QtWidgets.QLabel(self.frame_3)
            self.label_12.setObjectName("label_12")
            self.horizontalLayout_2.addWidget(self.label_12)
            self.label_12.setText(_translate("MainWindow", fdHomeMoney))
            self.label_12.setStyleSheet("color: white;")


            # home team moneyline draftkings
            self.label_13 = QtWidgets.QLabel(self.frame_3)
            self.label_13.setObjectName("label_13")
            self.horizontalLayout_2.addWidget(self.label_13)
            self.label_13.setText(_translate("MainWindow", dkHomeMoney))
            self.label_13.setStyleSheet("color: white;")


            # fanduel under
            self.label_14 = QtWidgets.QLabel(self.frame_3)
            self.label_14.setObjectName("label_14")
            self.horizontalLayout_2.addWidget(self.label_14)
            self.label_14.setText(_translate("MainWindow", fdUnder))
            self.label_14.setStyleSheet("color: white;")


            # draftkings under
            self.label_15 = QtWidgets.QLabel(self.frame_3)
            self.label_15.setObjectName("label_15")
            self.horizontalLayout_2.addWidget(self.label_15)
            self.label_15.setText(_translate("MainWindow", dkUnder))
            self.label_15.setStyleSheet("color: white;")



            self.line = QtWidgets.QFrame(self.bottomFrame)
            self.line.setGeometry(QtCore.QRect(14, 117, 1005, 23))
            self.line.setFrameShape(QtWidgets.QFrame.HLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")
            self.line_2 = QtWidgets.QFrame(self.bottomFrame)
            self.line_2.setGeometry(QtCore.QRect(492, 129, 29, 972))
            self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_2.setObjectName("line_2")
            self.line_3 = QtWidgets.QFrame(self.bottomFrame)
            self.line_3.setGeometry(QtCore.QRect(712, 129, 29, 972))
            self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
            self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_3.setObjectName("line_3")
            self.line_4 = QtWidgets.QFrame(self.bottomFrame)
            self.line_4.setGeometry(QtCore.QRect(14, lineMedianY, 1005, 19))
            lineMedianY += 95
            self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
            self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line_4.setObjectName("line_4")

        self.label_22 = QtWidgets.QLabel(self.bottomFrame)
        self.label_22.setGeometry(QtCore.QRect(280, 70, 71, 21))
        self.label_22.setText("Spread")
        self.label_22.setStyleSheet("color: white;")
        self.label_22.move(365, 100)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")

        self.label_23 = QtWidgets.QLabel(self.bottomFrame)
        self.label_23.setGeometry(QtCore.QRect(440, 70, 91, 21))
        self.label_23.setText("Moneyline")
        self.label_23.setStyleSheet("color: white;")
        self.label_23.move(580,100)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")

        self.label_24 = QtWidgets.QLabel(self.bottomFrame)
        self.label_24.setGeometry(QtCore.QRect(590, 70, 101, 21))
        self.label_24.setText("Over/Under")
        self.label_24.setStyleSheet("color: white;")
        self.label_24.move(798,100)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")

        # starting at label 16 - they don't move - they are the main headers for the data
        self.label_16 = QtWidgets.QLabel(self.bottomFrame)
        self.label_16.setGeometry(QtCore.QRect(250, 90, 61, 16))
        self.label_16.setObjectName("label_16")
        self.label_16.move(310,100)
        pixmap = QPixmap('C:/ProjectV2/images/fanduel_logo.png')
        self.label_16.setPixmap(pixmap)
        self.label_16.setFixedSize(pixmap.size())
        self.label_16.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.label_17 = QtWidgets.QLabel(self.bottomFrame)
        self.label_17.setGeometry(QtCore.QRect(410, 90, 61, 16))
        self.label_17.setObjectName("label_17")
        self.label_17.move(420,100)
        pixmap = QPixmap("C:/ProjectV2/images/draftkings.png")
        self.label_17.setPixmap(pixmap)
        self.label_17.setFixedSize(pixmap.size())
        self.label_17.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)



        self.label_18 = QtWidgets.QLabel(self.bottomFrame)
        self.label_18.setGeometry(QtCore.QRect(570, 90, 61, 16))
        self.label_18.setObjectName("label_18")
        self.label_18.move(540,100)
        pixmap = QPixmap("C:/ProjectV2/images/fanduel_logo.png")
        self.label_18.setPixmap(pixmap)
        self.label_18.setFixedSize(pixmap.size())
        self.label_18.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)



        self.label_19 = QtWidgets.QLabel(self.bottomFrame)
        self.label_19.setGeometry(QtCore.QRect(330, 90, 61, 16))
        self.label_19.setObjectName("label_19")
        self.label_19.move(650,100)
        pixmap = QPixmap("C:/ProjectV2/images/draftkings.png")
        self.label_19.setPixmap(pixmap)
        self.label_19.setFixedSize(pixmap.size())
        self.label_19.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)



        self.label_20 = QtWidgets.QLabel(self.bottomFrame)
        self.label_20.setGeometry(QtCore.QRect(490, 90, 61, 16))
        self.label_20.setObjectName("label_20")
        self.label_20.move(760,100)
        pixmap = QPixmap("C:/ProjectV2/images/fanduel_logo.png")
        self.label_20.setPixmap(pixmap)
        self.label_20.setFixedSize(pixmap.size())
        self.label_20.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)



        self.label_21 = QtWidgets.QLabel(self.bottomFrame)
        self.label_21.setGeometry(QtCore.QRect(650, 90, 61, 16))
        self.label_21.setObjectName("label_21")
        self.label_21.move(870,100)
        pixmap = QPixmap("C:/ProjectV2/images/draftkings.png")
        self.label_21.setPixmap(pixmap)
        self.label_21.setFixedSize(pixmap.size())
        self.label_21.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


        # Adding the header label
        self.headerLabel = QtWidgets.QLabel(self.bottomFrame)
        self.headerLabel.setGeometry(QtCore.QRect(325,50,1000,50))
        self.headerLabel.setText("NBA Real Time Betting Odds")
        self.headerLabel.setStyleSheet("font-size: 30px; color: white;")

        # Adding the gameID search bar:

        self.search_edit = QLineEdit(self.bottomFrame)

        self.search_edit.move(140,100)
        self.search_edit.setStyleSheet("background-color: white;")
        self.search_edit.setFixedHeight(20)
        self.search_edit.setFixedWidth(70)
        # Create a QPushButton widget to perform the search
        self.search_button = QPushButton(self.bottomFrame)
        self.search_button.setText("Search")
        self.search_button.move(215,100)
        self.search_button.setFixedHeight(20)
        self.search_button.setFixedWidth(40)

        self.search_button.setStyleSheet("background-color:white;")
        self.search_button.clicked.connect(self.getSearchTerm)

        # Creating a label to describe what the search bar does
        self.labelDesc = QtWidgets.QLabel(self.bottomFrame)
        self.labelDesc.setText("Enter a gameID to view odds history")
        self.labelDesc.move(140,85)
        self.labelDesc.setStyleSheet("color:white; font-size: 7px;")

        # Adding the live logo
        self.liveLabel = QtWidgets.QLabel(self.bottomFrame)
        self.liveLabel.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.liveLabel.setText("-Live-")
        self.liveLabel.setStyleSheet("font-size: 16px; color: red")
        self.liveLabel.move(30, 100)
        #pixmap = QPixmap("C:/ProjectV2/images/livelogo.jpg")
        # self.liveLabel.setPixmap(pixmap)
        # self.liveLabel.setFixedSize(pixmap.size())

        self.verticalLayout_2.addWidget(self.bottomFrame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

            #self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # # The home button
        homeButton = QtWidgets.QPushButton(self.bottomFrame, clicked = lambda:openHome(self))
        homeButton.setGeometry(0,0,100,50)
        homeButton.setText("Home")
        homeButton.setStyleSheet("background-color: transparent; color: white; font-size: 18px;")
        homeButton.setCursor(QCursor(Qt.PointingHandCursor))

        # The "How it works button
        howButton = QtWidgets.QPushButton(self.bottomFrame, clicked = lambda:openHow(self)) # CHANGE THIS TO THE CORRECT FUNCTION TO DISPLAY HOW IT WORKS
        howButton.setGeometry(100,0,150,50)
        howButton.setText("How it works")
        howButton.setStyleSheet("background-color: transparent; color: white; font-size: 18px;")
        howButton.setCursor(QCursor(Qt.PointingHandCursor))

        # The Live Scoring Page
        liveButton = QtWidgets.QPushButton(self.bottomFrame, clicked = lambda:openLive(self))
        liveButton.setGeometry(275,0,100,50)
        liveButton.setText("Live Scoring")
        liveButton.setStyleSheet("background-color: transparent; color: white; font-size: 18px;")
        liveButton.setCursor(QCursor(Qt.PointingHandCursor))



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())