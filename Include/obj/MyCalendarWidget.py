# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets, QCalendarWidget, QToolButton


class MyCalendarWidget(QCalendarWidget):
    def __init__(self):
        super().__init__()
        pass

    def updateIcons(self):
        QToolButton prevMonth =
