# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewProjectDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 242)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(400, 0))
        font = QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)

        self.lineEdit_NumeroON = QLineEdit(self.groupBox)
        self.lineEdit_NumeroON.setObjectName(u"lineEdit_NumeroON")

        self.gridLayout.addWidget(self.lineEdit_NumeroON, 2, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.lineEdit_OreDisponibili = QLineEdit(self.groupBox)
        self.lineEdit_OreDisponibili.setObjectName(u"lineEdit_OreDisponibili")

        self.gridLayout.addWidget(self.lineEdit_OreDisponibili, 5, 0, 1, 1)

        self.pushButton_Cerca = QPushButton(self.groupBox)
        self.pushButton_Cerca.setObjectName(u"pushButton_Cerca")

        self.gridLayout.addWidget(self.pushButton_Cerca, 1, 2, 1, 1)

        self.lineEdit_Equip = QLineEdit(self.groupBox)
        self.lineEdit_Equip.setObjectName(u"lineEdit_Equip")
        self.lineEdit_Equip.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_Equip, 1, 0, 1, 1)

        self.lineEdit_ClienteID = QLineEdit(self.groupBox)
        self.lineEdit_ClienteID.setObjectName(u"lineEdit_ClienteID")

        self.gridLayout.addWidget(self.lineEdit_ClienteID, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)

        self.textEdit_Descrizione = QTextEdit(self.groupBox)
        self.textEdit_Descrizione.setObjectName(u"textEdit_Descrizione")

        self.gridLayout.addWidget(self.textEdit_Descrizione, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Nuovo Progetto", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Ore a disposizione", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Equipment", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"ON", None))
        self.pushButton_Cerca.setText(QCoreApplication.translate("Dialog", u"Cerca", None))
        self.lineEdit_Equip.setPlaceholderText(QCoreApplication.translate("Dialog", u"Utilizza la funzione cerca", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Descrizione", None))
    # retranslateUi

