# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QWidget
from Include.uis.pagine.ui_paginaEdit import Ui_paginaEdit


class PaginaEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_paginaEdit()
        # self.widgetOrologio. = Orologio()
        self.ui.setupUi(self)
