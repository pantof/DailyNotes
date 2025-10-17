# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NuovoEquipmentDialog.ui'
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
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(70, 60, 208, 161))
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.lineEdit_NumeroEquip = QLineEdit(self.groupBox)
        self.lineEdit_NumeroEquip.setObjectName(u"lineEdit_NumeroEquip")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lineEdit_NumeroEquip)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)

        self.lineEdit_Via = QLineEdit(self.groupBox)
        self.lineEdit_Via.setObjectName(u"lineEdit_Via")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lineEdit_Via)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)

        self.lineEdit_NAP = QLineEdit(self.groupBox)
        self.lineEdit_NAP.setObjectName(u"lineEdit_NAP")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lineEdit_NAP)

        self.lineEdit_Comune = QLineEdit(self.groupBox)
        self.lineEdit_Comune.setObjectName(u"lineEdit_Comune")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lineEdit_Comune)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_4)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Equipment", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Numero", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Via", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"NAP", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Comune", None))
    # retranslateUi

