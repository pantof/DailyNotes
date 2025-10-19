# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class RiepilogoItemWidget(QWidget):
    """
    Widget personalizzato per visualizzare le due righe
    del riepilogo intervento in Pagina1.
    """
    def __init__(self, riga1, riga2):
        super().__init__()

        # Etichette
        self.label_riga1 = QLabel(riga1)
        self.label_riga1.setStyleSheet("font-weight: bold;")
        self.label_riga1.setWordWrap(True) # Permetti alla riga 1 di andare a capo

        self.label_riga2 = QLabel(riga2)
        # Usiamo il padding-left per creare il rientro
        self.label_riga2.setStyleSheet("padding-left: 15px;")
        self.label_riga2.setWordWrap(True) # Permetti alla riga 2 di andare a capo

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_riga1)
        layout.addWidget(self.label_riga2)
        layout.setContentsMargins(5, 3, 5, 3) # Un po' di spazio
        layout.setSpacing(1) # Spazio minimo tra le due righe

        self.setLayout(layout)
