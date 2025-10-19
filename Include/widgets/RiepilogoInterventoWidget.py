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
    def __init__(self, intervento_id, progetto_on, descrizione, ora_inizio, ora_fine, ore):
        super().__init__()

        # --- MEMORIZZA I DATI ---
        self.intervento_id = intervento_id
        self.progetto_on = progetto_on
        self.descrizione = descrizione
        self.ore = ore
        # ------------------------

        testo = (f"{descrizione} "
                 f"({ora_inizio} - {ora_fine}, {ore:.2f} ore)")

        label = QLabel(testo)
        label.setStyleSheet("padding-left: 20px;")
        label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.setContentsMargins(5, 0, 5, 3)
        layout.setSpacing(0)
        self.setLayout(layout)
