# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagina2.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Pagina02(object):
    def setupUi(self, Pagina02):
        if not Pagina02.objectName():
            Pagina02.setObjectName(u"Pagina02")
        Pagina02.resize(720, 448)
        Pagina02.setMinimumSize(QSize(720, 0))
        self.verticalLayout = QVBoxLayout(Pagina02)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(Pagina02)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(710, 0))

        self.verticalLayout.addWidget(self.listWidget)


        self.retranslateUi(Pagina02)

        QMetaObject.connectSlotsByName(Pagina02)
    # setupUi

    def retranslateUi(self, Pagina02):
        Pagina02.setWindowTitle(QCoreApplication.translate("Pagina02", u"Form", None))
    # retranslateUi

