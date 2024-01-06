# This Python file uses the following encoding: utf-8
# import sys
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, QTime

from Include.uis.LCDclock.ui_LCDclock import Ui_Orologio

class Orologio(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Orologio()
        self.ui.setupUi(self)
        timer = QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)
        self.showlcd()
#        style = """
#                    QLCDNumber {
#                        border: 2px solid black;
#                        background-color: yellow;
#                        color: red;
#                    }
#                """
#        self.ui.lcdNumberClock.setStyleSheet(style)

    def showlcd(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        self.ui.lcdNumberClock.display(text)

# if __name__ == "__main__":
#     pass
