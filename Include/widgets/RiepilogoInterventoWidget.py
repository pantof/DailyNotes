# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class RiepilogoInterventoWidget(QWidget):
    """
    Widget per il singolo intervento nel riepilogo di Pagina1.
    Mostra la descrizione e i dettagli orari, con un rientro.
    """
    def __init__(self, descrizione, ora_inizio, ora_fine, ore):
        super().__init__()

        # Testo (es. "Manutenzione (09:00 - 11:30, 2.50 ore)")
        testo = (f"{descrizione} "
                 f"({ora_inizio} - {ora_fine}, {ore:.2f} ore)")

        label = QLabel(testo)
        # Rientro per allinearlo sotto l'intestazione
        label.setStyleSheet("padding-left: 20px;")
        label.setWordWrap(True)

        # Layout verticale (anche se c'è solo una label,
        # ci permette di controllare i margini)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.setContentsMargins(5, 0, 5, 3) # Spazio solo sotto
        layout.setSpacing(0)
        self.setLayout(layout)
