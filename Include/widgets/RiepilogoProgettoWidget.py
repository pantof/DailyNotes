# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt

class RiepilogoProgettoWidget(QWidget):
    """
    Widget per l'intestazione di un progetto nel riepilogo di Pagina1.
    Mostra il nome del progetto e le ore totali per quel progetto.
    """
    def __init__(self, progetto_on, nome_cliente, ore_totali):
        super().__init__()

        # Testo principale (es. "[ON-123] - Azienda Cliente")
        self.progetto_on = progetto_on
        self.nome_cliente = nome_cliente
        testo_progetto = f"[{progetto_on}] - {nome_cliente}"
        label_progetto = QLabel(testo_progetto)
        label_progetto.setStyleSheet("font-weight: bold; font-size: 10pt;")
        label_progetto.setWordWrap(True)

        # Testo ore (es. "Totale: 3.50 ore")
        testo_ore = f"Totale: {ore_totali:.2f} ore"
        label_ore = QLabel(testo_ore)
        label_ore.setStyleSheet("font-weight: bold; font-size: 10pt; padding-left: 10px;")
        label_ore.setAlignment(Qt.AlignRight) # Allinea a destra

        # Layout orizzontale
        layout = QHBoxLayout()
        layout.addWidget(label_progetto, 1) # Il nome occupa più spazio
        layout.addWidget(label_ore, 0)   # Le ore si adattano
        layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(layout)

        # Stile per far "staccare" l'intestazione
        self.setStyleSheet("background-color: #4a4a4a; border-radius: 3px;")
