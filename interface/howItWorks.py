# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'howItWorks.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#from interface import allGs, home


from openPages import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QToolBar,QSizePolicy
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QToolBar,QSizePolicy, QTextEdit
from PyQt5.QtGui import QColor, QCursor



class howItWorks(object):
    # def openHome(self):
    #
    #     self.window = QtWidgets.QMainWindow()
    #
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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #333333;")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 786, 550))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setMinimumSize(QtCore.QSize(0, 1800))
        self.frame.setStyleSheet("background-color: #333333;")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(350, 50, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(100, 100, 800, 81))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText("Use this page to help learn how to work with Edge Finder. "
                              "This simply will help you understand how to navigate the software.\n "
                              "At the bottom of the page, you can find resources that will help "
                              "explain how to make the best use of the information that is provided")
        self.textEdit.setStyleSheet("font-size: 12px; font-style: italic; color: white;")
        self.textEdit.setAlignment(Qt.AlignCenter)


        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 200, 800, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        #self.label_2.setStyleSheet("text-alignment: center;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        # Label to show 'how to' step 1 image
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(25, 200, 511, 251))
        self.label_3.setObjectName("label_3")
        self.label_3.move(25,250)
        pixmap = QPixmap("C:/ProjectV2/images/how_to_step1.png")
        self.label_3.setPixmap(pixmap)
        self.label_3.setFixedSize(pixmap.size())
        self.label_3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Text Edit to help explain step 1
        self.textEdit2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit2.setGeometry(550, 250, 350,250)
        self.textEdit2.setText("From any point in the software, you will be able to navigate to any of the pages that are available "
                               "to view. The first step in being able to analyze real time sports betting data is to navigate to the "
                               "Live Scores Page which will always be displayed in the upper menu throughout the application. As of now "
                               "the only available sport for viewing is the NBA - but in the future, there will be more options available "
                               "for you to view.")
        self.textEdit2.setAlignment(Qt.AlignCenter)
        self.textEdit2.setStyleSheet("font-size: 12pt;color: white;")

        # Label for words for step 2
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 515, 600, 41))
        self.label_4.setText("Step 2: Navigate the available games")
        self.label_4.setStyleSheet("font-size: 10pt; font-weight: bold; color: white;")

        # Label to show example image for step 2
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(25, 200, 511, 251))
        self.label_5.setObjectName("label_3")
        self.label_5.move(25,570)
        pixmap = QPixmap("C:/ProjectV2/images/how_to_step2.png")
        self.label_5.setPixmap(pixmap)
        self.label_5.setFixedSize(pixmap.size())
        self.label_5.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Text edit to help explain step 2
        self.textEdit3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit3.setGeometry(550, 570, 350,250)
        self.textEdit3.setText("Once you have reached the Live Scores Page: \n"
                               "- You can browse all of the available games as they are showed on either sportsbook (DraftKings or Fanduel)\n "
                               "- The three main markets are displayed for every game (spread, moneyline, over/under) \n"
                               "- The data that is being displayed on this page is the most recent data that has been gathered from the "
                               "real time odds scraper that is being run over both sportsbooks. \n "
                               "- Each game is also given a unique gameID and is displayed under each teams names. GameId's are unique for every "
                               "game, on every day. So it is important to take note of the current gameID for the game in question.\n"
                               "- This gameID can be used to view historical odds movement for the game in question.\n"
                               )

        self.textEdit3.setStyleSheet("font-size: 10pt; color: white;")

        # Label for step 3 header
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(70, 850, 600, 41))
        self.label_6.setText("Step 3: Search for the game desired")
        self.label_6.setStyleSheet("font-size: 10pt; font-weight: bold; color: white;")

        # Label to show example image for step 3
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(25, 200, 511, 251))
        self.label_7.setObjectName("label_3")
        self.label_7.move(25,890)
        pixmap = QPixmap("C:/ProjectV2/images/how_to_step3.png")
        self.label_7.setPixmap(pixmap)
        self.label_7.setFixedSize(pixmap.size())
        self.label_7.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Text edit to help explain step 2
        self.textEdit4 = QtWidgets.QTextEdit(self.frame)
        self.textEdit4.setGeometry(550, 890, 350,250)
        self.textEdit4.setText("- Given the gameID mentioned in the previous section. This can be used to view the historical"
                               "odds movement for both the spread and the moneyline on each sportsbook.\n"
                               "- Copy and past any gameID into the search bar at the top of the page and a window will appear showing"
                               " line charts of how the data has moved, since the game was first made available for viewing. \n"
                               "- A separate line is created and color coded for the sportsbook that the data originates from. Given this"
                               " data beind viewd in real time can help gain a statistical advantage on bets that could be high value in the "
                               "moment, but also just to view the nature of how the data moves across two different companies, and that can be "
                               "studied and use in future endeavors.")
        self.textEdit4.setStyleSheet("font-size: 10pt;color: white;")


        # other helpful links header
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(350, 1200, 600, 41))
        self.label_8.setText("Other Helpful Links")
        self.label_8.setStyleSheet("font-size: 20pt; font-weight: bold; color: white;")

        # Displaying the first helpful video
        self.video = QWebEngineView(self.frame)
        self.video.setGeometry(QtCore.QRect(25, 1250, 400, 250))
        self.video.setObjectName("video")
        self.video.load(QtCore.QUrl("https://www.youtube.com/embed/wiOq8MbVRws"))

        # Displaying the second helpful video
        self.video2 = QWebEngineView(self.frame)
        self.video2.setGeometry(QtCore.QRect(500, 1250, 400, 250))
        self.video2.setObjectName("video")
        self.video2.load(QtCore.QUrl("https://www.youtube.com/embed/jrdhS3KB4Qk"))

        # Displaying the third helpful video
        self.video3 = QWebEngineView(self.frame)
        self.video3.setGeometry(QtCore.QRect(250, 1550, 400, 250))
        self.video3.setObjectName("video")
        self.video3.load(QtCore.QUrl("https://www.youtube.com/embed/EPwzirlb2rI"))


        # Adding the menu buttons to the top

        # The home button
        homeButton = QtWidgets.QPushButton(self.frame, clicked = lambda:openHome(self))
        homeButton.setGeometry(0,0,100,50)
        homeButton.setText("Home")
        homeButton.setStyleSheet("background-color: transparent; color: white; font-size: 18px;")
        homeButton.setCursor(QCursor(Qt.PointingHandCursor))

        # The "How it works button
        howButton = QtWidgets.QPushButton(self.frame, clicked = lambda:openHow(self)) # CHANGE THIS TO THE CORRECT FUNCTION TO DISPLAY HOW IT WORKS
        howButton.setGeometry(100,0,150,50)
        howButton.setText("How it works")
        howButton.setStyleSheet("background-color: transparent; color: white; font-size: 18px;")
        howButton.setCursor(QCursor(Qt.PointingHandCursor))

        # The Live Scoring Page
        liveButton = QtWidgets.QPushButton(self.frame, clicked = lambda:openLive(self))
        liveButton.setGeometry(275,0,100,50)
        liveButton.setText("Live Scoring")
        liveButton.setStyleSheet("background-color: transparent; color: white; font-size: 18px;")
        liveButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "How to use Edge Finder"))
        self.label_2.setText(_translate("MainWindow", "Step 1: Navigate to the live scoring page from any point in the software -"
                                                        " located in top main menu bar"))
        self.label_2.setStyleSheet("color: white;")
        self.label.setStyleSheet("color: white;")

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.showMaximized()
#     MainWindow.show()
#     sys.exit(app.exec_())
