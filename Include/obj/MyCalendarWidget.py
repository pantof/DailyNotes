# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QCalendarWidget
from PySide6.QtGui import QPainter, QColor, QPolygon
from PySide6.QtCore import QDate, QPoint

class MyCalendarWidget(QCalendarWidget):
    """
    Calendario personalizzato che disegna un indicatore
    sui giorni che contengono interventi.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dates_with_entries = set()

    def setDatesWithEntries(self, dates: set[QDate]):
        """
        Imposta l'elenco delle date che devono avere un indicatore.
        """
        self.dates_with_entries = dates
        self.updateCells() # Richiede un ridisegno

    def paintCell(self, painter: QPainter, rect, date: QDate):
        """
                Sovrascrive la funzione di disegno per aggiungere un triangolo.
        """
        # 1. Disegna la cella base (numeri, sfondo, ecc.)
        super().paintCell(painter, rect, date)
        # 2. Se la data è nel nostro set, disegna il triangolo
        if date in self.dates_with_entries:
            painter.save()
            painter.setBrush(QColor("cyan"))
            painter.setPen(QColor("cyan"))
            size = 10
            triangle = QPolygon([
                QPoint(rect.left(), rect.bottom()),
                QPoint(rect.left() + size, rect.bottom()),
                QPoint(rect.left(), rect.bottom() - size)
            ])
#            triangle = QPolygon([
#                            QPoint(rect.right() - size, rect.bottom()),
#                            QPoint(rect.right(), rect.bottom() - size),
#                            QPoint(rect.right(), rect.bottom())
#            ])
            painter.drawPolygon(triangle)
            painter.restore()





