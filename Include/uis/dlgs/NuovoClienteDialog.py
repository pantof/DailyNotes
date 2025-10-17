# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QDialog
from Include.uis.dlgs.ui_NuovoClienteDialog import Ui_Dialog

class NuovoClienteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def get_data(self):
        """
                Recupera i dati dai campi del dialogo e li
                restituisce come dizionario.
        """
        try:
            data = {
                # Dati Cliente
                "Azienda": self.ui.lineEdit_Azienda.text(),
                "Nome": self.ui.lineEdit_Nome.text(),
                "Cognome": self.ui.lineEdit_Cognome.text(),
                # Dati Indirizzo
                "Via": self.ui.lineEdit_Via.text(),
                "NAP": self.ui.lineEdit_NAP.text(),
                "Comune": self.ui.lineEdit_Comune.text(),
            }
            return data
        except AttributeError as e:
            print(f"Errore: Nomi widget in NuovoClienteDialog.py non corretti! {e}")
            return None

