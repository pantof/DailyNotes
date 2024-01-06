# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog
from Include.uis.dlgs.ui_NewProjectDialog import Ui_Dialog


class NewProjectDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
