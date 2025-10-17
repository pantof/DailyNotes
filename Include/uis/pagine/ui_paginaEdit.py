# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paginaEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_paginaEdit(object):
    def setupUi(self, paginaEdit):
        if not paginaEdit.objectName():
            paginaEdit.setObjectName(u"paginaEdit")
        paginaEdit.resize(514, 376)
        self.gridLayout = QGridLayout(paginaEdit)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_3 = QPushButton(paginaEdit)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)

        self.label = QLabel(paginaEdit)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(paginaEdit)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)

        self.pushButton_1 = QPushButton(paginaEdit)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.gridLayout.addWidget(self.pushButton_1, 2, 0, 1, 1)


        self.retranslateUi(paginaEdit)

        QMetaObject.connectSlotsByName(paginaEdit)
    # setupUi

    def retranslateUi(self, paginaEdit):
        paginaEdit.setWindowTitle(QCoreApplication.translate("paginaEdit", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("paginaEdit", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("paginaEdit", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("paginaEdit", u"PushButton", None))
        self.pushButton_1.setText(QCoreApplication.translate("paginaEdit", u"Inserisci nuovo progetto", None))
    # retranslateUi

