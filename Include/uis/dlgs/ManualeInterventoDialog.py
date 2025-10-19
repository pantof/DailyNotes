# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from PySide6.QtWidgets import (QDialog, QDialogButtonBox, QVBoxLayout, QFormLayout, QLabel, QDoubleSpinBox)

class ManualeInterventoDialog(QDialog):
    """
    Dialogo per inserire manualmente un intervento (solo durata).
    """
    def __init__(self, progetto_on, nome_cliente, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Inserimento Manuale")

        # Layout principale
        layout = QVBoxLayout(self)

        # Etichette informative
        info_label = QLabel(f"Progetto: [{progetto_on}] - {nome_cliente}\nData: {data}")
        info_label.setStyleSheet("font-weight: bold;")

        # Form per l'input
        form_layout = QFormLayout()
        self.spinBox_ore = QDoubleSpinBox()
        self.spinBox_ore.setDecimals(2)
        self.spinBox_ore.setMinimum(0.01)
        self.spinBox_ore.setMaximum(24)
        self.spinBox_ore.setValue(1.0)
        form_layout.addRow("Ore lavorate:", self.spinBox_ore)

        # Pulsanti OK/Annulla
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        # Assemblaggio
        layout.addWidget(info_label)
        layout.addLayout(form_layout)
        layout.addWidget(buttonBox)

    def get_ore(self):
        """ Restituisce il numero di ore inserito. """
        return self.spinBox_ore.value()
