# This Python file uses the following encoding: utf-8
# from PySide6 import QtCore
from PySide6.QtCore import QTimer, QTime
from PySide6 import QtWidgets
from Include.uis.Orologio.ui_DisplyOrologio import Ui_OrologioDisplay


class DisplayOrologio(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_OrologioDisplay()
        self.ui.setupUi(self)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime() # color='darkCyan'
        style = """
                            QLabel {
                                color: darkCyan;
                            }
                        """
        self.ui.labelOrologio.setStyleSheet(style)

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        self.ui.labelOrologio.setText(text)
