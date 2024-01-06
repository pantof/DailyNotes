# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DisplyOrologio.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_OrologioDisplay(object):
    def setupUi(self, OrologioDisplay):
        if not OrologioDisplay.objectName():
            OrologioDisplay.setObjectName(u"OrologioDisplay")
        OrologioDisplay.resize(180, 136)
        self.verticalLayout = QVBoxLayout(OrologioDisplay)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelOrologio = QLabel(OrologioDisplay)
        self.labelOrologio.setObjectName(u"labelOrologio")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.labelOrologio.setFont(font)
        self.labelOrologio.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelOrologio)


        self.retranslateUi(OrologioDisplay)

        QMetaObject.connectSlotsByName(OrologioDisplay)
    # setupUi

    def retranslateUi(self, OrologioDisplay):
        OrologioDisplay.setWindowTitle(QCoreApplication.translate("OrologioDisplay", u"Form", None))
        self.labelOrologio.setText("")
    # retranslateUi

