# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagina1.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCalendarWidget, QComboBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QSizePolicy, QSpacerItem, QSpinBox, QToolButton,
    QVBoxLayout, QWidget)

from Include.obj.MyCalendarWidget import MyCalendarWidget

class Ui_Pagina01(object):
    def setupUi(self, Pagina01):
        if not Pagina01.objectName():
            Pagina01.setObjectName(u"Pagina01")
        Pagina01.resize(834, 509)
        font = QFont()
        font.setPointSize(14)
        Pagina01.setFont(font)
        self.verticalLayout = QVBoxLayout(Pagina01)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.labelData = QLabel(Pagina01)
        self.labelData.setObjectName(u"labelData")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.labelData.setFont(font1)

        self.horizontalLayout.addWidget(self.labelData)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.prevMonth = QToolButton(Pagina01)
        self.prevMonth.setObjectName(u"prevMonth")
        self.prevMonth.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.prevMonth)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.mesi = QComboBox(Pagina01)
        self.mesi.addItem("")
        self.mesi.addItem("")
        self.mesi.addItem("")
        self.mesi.addItem("")
        self.mesi.addItem("")
        self.mesi.addItem("")
        self.mesi.addItem("")
        self.mesi.addItem("")
        self.mesi.addItem("")
        self.mesi.addItem("")
        self.mesi.addItem("")
        self.mesi.addItem("")
        self.mesi.setObjectName(u"mesi")
        self.mesi.setMinimumSize(QSize(1, 0))
        self.mesi.setFont(font1)

        self.horizontalLayout_2.addWidget(self.mesi)

        self.spinBoxAnno = QSpinBox(Pagina01)
        self.spinBoxAnno.setObjectName(u"spinBoxAnno")
        self.spinBoxAnno.setFont(font1)
        self.spinBoxAnno.setReadOnly(False)
        self.spinBoxAnno.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.spinBoxAnno.setKeyboardTracking(True)
        self.spinBoxAnno.setMinimum(2010)
        self.spinBoxAnno.setMaximum(9999)

        self.horizontalLayout_2.addWidget(self.spinBoxAnno)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.nextMonth = QToolButton(Pagina01)
        self.nextMonth.setObjectName(u"nextMonth")
        self.nextMonth.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.nextMonth)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.calendarWidget = MyCalendarWidget(Pagina01)
        self.calendarWidget.setObjectName(u"calendarWidget")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        font2.setHintingPreference(QFont.PreferNoHinting)
        self.calendarWidget.setFont(font2)
        self.calendarWidget.setStyleSheet(u"")
        self.calendarWidget.setMinimumDate(QDate(2010, 9, 14))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.LongDayNames)
        self.calendarWidget.setNavigationBarVisible(False)

        self.verticalLayout.addWidget(self.calendarWidget)

        self.listWidget_Riepilogo = QListWidget(Pagina01)
        self.listWidget_Riepilogo.setObjectName(u"listWidget_Riepilogo")

        self.verticalLayout.addWidget(self.listWidget_Riepilogo)


        self.retranslateUi(Pagina01)
        self.nextMonth.clicked.connect(self.calendarWidget.showNextMonth)
        self.prevMonth.clicked.connect(self.calendarWidget.showPreviousMonth)

        QMetaObject.connectSlotsByName(Pagina01)
    # setupUi

    def retranslateUi(self, Pagina01):
        Pagina01.setWindowTitle(QCoreApplication.translate("Pagina01", u"Form", None))
        self.labelData.setText(QCoreApplication.translate("Pagina01", u"TextLabel", None))
        self.prevMonth.setText("")
        self.mesi.setItemText(0, QCoreApplication.translate("Pagina01", u"gennaio", None))
        self.mesi.setItemText(1, QCoreApplication.translate("Pagina01", u"febbraio", None))
        self.mesi.setItemText(2, QCoreApplication.translate("Pagina01", u"marzo", None))
        self.mesi.setItemText(3, QCoreApplication.translate("Pagina01", u"aprile", None))
        self.mesi.setItemText(4, QCoreApplication.translate("Pagina01", u"maggio", None))
        self.mesi.setItemText(5, QCoreApplication.translate("Pagina01", u"giugno", None))
        self.mesi.setItemText(6, QCoreApplication.translate("Pagina01", u"luglio", None))
        self.mesi.setItemText(7, QCoreApplication.translate("Pagina01", u"agosto", None))
        self.mesi.setItemText(8, QCoreApplication.translate("Pagina01", u"settembre", None))
        self.mesi.setItemText(9, QCoreApplication.translate("Pagina01", u"ottobre", None))
        self.mesi.setItemText(10, QCoreApplication.translate("Pagina01", u"novembre", None))
        self.mesi.setItemText(11, QCoreApplication.translate("Pagina01", u"dicembre", None))

        self.nextMonth.setText("")
    # retranslateUi

