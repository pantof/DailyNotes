# This Python file uses the following encoding: utf-8
# import sys
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, QDate, Qt
from PySide6.QtGui import QTextCharFormat, QColor, QBrush, QPalette
# from PySide6 import Qt
# void QCalendarWidget::setCurrentPage(int year, int month)

from Include.uis.pagine.ui_pagina1 import Ui_Pagina01
# from Include.uis.LCDclock.LCDclock import Orologio

from Include.func.changeColor import changeSVGColor
"""
https://stackoverflow.com/questions/60659643/how-to-change-the-background-colour-of-a-cell-in-a-qcalendarwidget-using-an-sql
https://stackoverflow.com/questions/56253427/coloring-pyqt5-qcalendarwidget-cell-and-printing-data-inside-the-cells?noredirect=1&lq=1
https://stackoverflow.com/questions/58165586/highlight-date-interval-in-a-qt5-calendar-widget?noredirect=1&lq=1

"""


class PaginaHome(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Pagina01()
        # self.widgetOrologio. = Orologio()
        self.ui.setupUi(self)
        self.now = QDate.currentDate()
        self.ui.spinBoxAnno.setValue(self.now.year())
        self.ui.mesi.setCurrentIndex(self.now.month()-1)
        self.ui.labelData.setText(self.now.toString("dd.MM.yyyy"))
        # print(self.now.month()-1)
        calendarPalette = QPalette()
        calendarPalette.setColor(QPalette.Text, QColor(255, 255, 255))
        self.sundayFormat = QTextCharFormat()
        # calendarPalette.setColor(
        # self.saturdayFormat = QTextCharFormat()
        self.sundayFormat.setForeground(QBrush(QColor("cyan")))
        self.ui.calendarWidget.setWeekdayTextFormat(
            Qt.DayOfWeek.Sunday, self.sundayFormat)
        self.ui.calendarWidget.setWeekdayTextFormat(
            Qt.DayOfWeek.Saturday, self.sundayFormat)
        # self.ui.calendarWidget.setba
        self.ui.calendarWidget.setPalette(calendarPalette)

        self.ui.nextMonth.setIcon(
            changeSVGColor(":/svg/Include/ico/arrow-right.svg"))
        self.ui.prevMonth.setIcon(
            changeSVGColor(":/svg/Include/ico/arrow-left.svg"))
        self.ui.mesi.currentIndexChanged.connect(self.meseCambiato)
        self.ui.calendarWidget.currentPageChanged.connect(
            self.dataCambiataDaCalendario)
        self.ui.calendarWidget.selectionChanged.connect(
            self.cambioSelezioneCalendario)
        self.ui.spinBoxAnno.valueChanged.connect(self.cambioDataDaSpinBox)

    @Slot()
    def meseCambiato(self):
        # Cambio mese da combo a Calendario
        # print(self.ui.mesi.currentText())
        # print(self.ui.mesi.currentIndex()+1)
        self.ui.calendarWidget.setCurrentPage(
            self.ui.spinBoxAnno.value(), self.ui.mesi.currentIndex()+1)

    @Slot()
    def dataCambiataDaCalendario(self):
        self.ui.mesi.setCurrentIndex(self.ui.calendarWidget.monthShown()-1)
        self.ui.spinBoxAnno.setValue(self.ui.calendarWidget.yearShown())
        self.ui.labelData.setText(
            self.ui.calendarWidget.selectedDate().toString("dd.MM.yyyy"))
        # Cambio data da calendario a combo

    @Slot()
    def cambioDataDaSpinBox(self):
        self.ui.calendarWidget.setCurrentPage(
            self.ui.spinBoxAnno.value(), self.ui.mesi.currentIndex()+1)

    @Slot()
    def cambioSelezioneCalendario(self):
        self.ui.labelData.setText(
            self.ui.calendarWidget.selectedDate().toString("dd.MM.yyyy"))


if __name__ == "__main__":
    pass
