import sys
from mainwindow import MainWindow
from PyQt6.QtWidgets import QApplication
import pydirectinput

pydirectinput.PAUSE = 0
pydirectinput.MINIMUM_SLEEP = 0
pydirectinput.MINIMUM_DURATION = 0

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()