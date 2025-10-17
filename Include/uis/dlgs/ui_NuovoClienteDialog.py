# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NuovoClienteDialog.ui'
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
    QFormLayout, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(262, 273)
        font = QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.lineEdit_Azienda = QLineEdit(self.groupBox)
        self.lineEdit_Azienda.setObjectName(u"lineEdit_Azienda")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lineEdit_Azienda)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)

        self.lineEdit_Nome = QLineEdit(self.groupBox)
        self.lineEdit_Nome.setObjectName(u"lineEdit_Nome")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lineEdit_Nome)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)

        self.lineEdit_Cognome = QLineEdit(self.groupBox)
        self.lineEdit_Cognome.setObjectName(u"lineEdit_Cognome")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lineEdit_Cognome)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_3)

        self.lineEdit_Via = QLineEdit(self.groupBox)
        self.lineEdit_Via.setObjectName(u"lineEdit_Via")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lineEdit_Via)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_4)

        self.lineEdit_NAP = QLineEdit(self.groupBox)
        self.lineEdit_NAP.setObjectName(u"lineEdit_NAP")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lineEdit_NAP)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_5)

        self.lineEdit_Comune = QLineEdit(self.groupBox)
        self.lineEdit_Comune.setObjectName(u"lineEdit_Comune")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lineEdit_Comune)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_6)


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
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Cliente", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Azienda", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nome", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Cognome", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Via", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"NAP", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Comune", None))
    # retranslateUi

