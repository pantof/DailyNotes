# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import Qt


class IndirizziModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._headers = list(self._data[0].keys())

    def data(self, index, role):
        if role == Qt.BackgroundRule and index.column() == 0:
            pass
            # column = index.column()
            # column_key = self._headers[column]
            # value = self._data[index.row()][column_key]
            # if isinstance(value, str):

    def headerData(self, section, orientation, role):
        pass
