from allGs import *
from howItWorks import *
from home import *

def openHome(MainWindow):
    window = QtWidgets.QMainWindow()

    ui = homePage()
    ui.setupUi(window)

    MainWindow.hide()
    window.showMaximized()
    window.show()

def openLive(MainWindow):
    window = QtWidgets.QMainWindow()
    ui = allGames()
    ui.setupUi(window)
    MainWindow.hide()
    window.showMaximized()
    window.show()

def openHow(MainWindow):
    window = QtWidgets.QMainWindow()
    ui = howItWorks()
    ui.setupUi(window)
    MainWindow.hide()
    window.showMaximized()
    window.show()
