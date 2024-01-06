# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'giornaliero.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(784, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(700, 80))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.labelEquip = QLabel(self.groupBox)
        self.labelEquip.setObjectName(u"labelEquip")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.labelEquip.setFont(font1)

        self.horizontalLayout.addWidget(self.labelEquip)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.labelNP = QLabel(self.groupBox)
        self.labelNP.setObjectName(u"labelNP")
        self.labelNP.setFont(font1)

        self.horizontalLayout.addWidget(self.labelNP)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.labelDescrizione = QLabel(self.groupBox)
        self.labelDescrizione.setObjectName(u"labelDescrizione")
        self.labelDescrizione.setFont(font1)

        self.horizontalLayout.addWidget(self.labelDescrizione)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonStop = QPushButton(self.groupBox)
        self.pushButtonStop.setObjectName(u"pushButtonStop")
        self.pushButtonStop.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButtonStop, 0, 1, 1, 1)

        self.pushButtonStart = QPushButton(self.groupBox)
        self.pushButtonStart.setObjectName(u"pushButtonStart")
        self.pushButtonStart.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButtonStart, 0, 0, 1, 1)

        self.pushButtonClose = QPushButton(self.groupBox)
        self.pushButtonClose.setObjectName(u"pushButtonClose")
        self.pushButtonClose.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButtonClose, 0, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(10)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Progetto", None))
        self.labelEquip.setText(QCoreApplication.translate("Form", u"TextLabel1111111111", None))
        self.labelNP.setText(QCoreApplication.translate("Form", u"TextLabel1111111111", None))
        self.labelDescrizione.setText(QCoreApplication.translate("Form", u"TextLabel1111111111", None))
#if QT_CONFIG(tooltip)
        self.pushButtonStop.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonStop.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonStart.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButtonStart.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.pushButtonStart.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.pushButtonStart.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonClose.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButtonClose.setText("")
    # retranslateUi

