# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewProjectDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(307, 190)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_2 = QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lineEdit_Equipment = QLineEdit(self.groupBox)
        self.lineEdit_Equipment.setObjectName(u"lineEdit_Equipment")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lineEdit_Equipment)

        self.lineEdit_ON = QLineEdit(self.groupBox)
        self.lineEdit_ON.setObjectName(u"lineEdit_ON")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lineEdit_ON)

        self.lineEdit_Descrizione = QLineEdit(self.groupBox)
        self.lineEdit_Descrizione.setObjectName(u"lineEdit_Descrizione")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lineEdit_Descrizione)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_3)

        self.lineEdit_Ore = QLineEdit(self.groupBox)
        self.lineEdit_Ore.setObjectName(u"lineEdit_Ore")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lineEdit_Ore)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_4)


        self.verticalLayout.addWidget(self.groupBox)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Nuovo Progetto", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Equipment", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"ON", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Descrizione", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Ore a disposizione", None))
    # retranslateUi

