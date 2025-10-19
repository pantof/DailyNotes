# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from PySide6.QtWidgets import (QDialog, QDialogButtonBox, QVBoxLayout,
                               QFormLayout, QLabel, QDoubleSpinBox, QLineEdit)

class ModificaInterventoDialog(QDialog):
    """
    Dialogo per modificare un intervento esistente.
    """
    def __init__(self, progetto_on, data, ore_attuali, descrizione_attuale, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifica Intervento")

        # Layout principale
        layout = QVBoxLayout(self)

        # Etichette informative
        info_label = QLabel(f"Progetto: [{progetto_on}]\nData: {data}")
        info_label.setStyleSheet("font-weight: bold;")

        # Form per l'input
        form_layout = QFormLayout()

        # Descrizione
        self.lineEdit_descrizione = QLineEdit(descrizione_attuale)
        form_layout.addRow("Descrizione:", self.lineEdit_descrizione)

        # Ore
        self.spinBox_ore = QDoubleSpinBox()
        self.spinBox_ore.setDecimals(2)
        self.spinBox_ore.setMinimum(0.01)
        self.spinBox_ore.setMaximum(24)
        self.spinBox_ore.setValue(ore_attuali)
        form_layout.addRow("Ore lavorate:", self.spinBox_ore)

        # Pulsanti OK/Annulla
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        # Assemblaggio
        layout.addWidget(info_label)
        layout.addLayout(form_layout)
        layout.addWidget(buttonBox)

    def get_data(self):
        """ Restituisce i nuovi dati inseriti. """
        return {
            "ore_nuove": self.spinBox_ore.value(),
            "descrizione_nuova": self.lineEdit_descrizione.text()
        }
