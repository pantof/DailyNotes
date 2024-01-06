# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LCDclock.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Orologio(object):
    def setupUi(self, Orologio):
        if not Orologio.objectName():
            Orologio.setObjectName(u"Orologio")
        Orologio.resize(120, 100)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        Orologio.setFont(font)
        self.verticalLayout = QVBoxLayout(Orologio)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lcdNumberClock = QLCDNumber(Orologio)
        self.lcdNumberClock.setObjectName(u"lcdNumberClock")
        self.lcdNumberClock.setFrameShape(QFrame.NoFrame)
        self.lcdNumberClock.setFrameShadow(QFrame.Plain)
        self.lcdNumberClock.setLineWidth(0)
        self.lcdNumberClock.setDigitCount(5)
        self.lcdNumberClock.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout.addWidget(self.lcdNumberClock)


        self.retranslateUi(Orologio)

        QMetaObject.connectSlotsByName(Orologio)
    # setupUi

    def retranslateUi(self, Orologio):
        Orologio.setWindowTitle(QCoreApplication.translate("Orologio", u"Form", None))
    # retranslateUi

