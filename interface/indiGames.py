from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create two labels and add them to the layout
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        layout.addWidget(label1)
        layout.addWidget(label2)

    def resizeEvent(self, event):
        # Adjust the size and position of the labels when the window is resized
        label1 = self.centralWidget().layout().itemAt(0).widget()
        label2 = self.centralWidget().layout().itemAt(1).widget()
        label1.setGeometry(10, 10, event.size().width()-20, event.size().height()/2-15)
        label2.setGeometry(10, event.size().height()/2+5, event.size().width()-20, event.size().height()/2-15)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
