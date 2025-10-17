# This Python file uses the following encoding: utf-8


from PySide6.QtWidgets import QDialog
from Include.uis.dlgs.ui_NuovoEquipmentDialog import Ui_Dialog
# se indirizzo esiste?


class NuovoEquipmentDialog(QDialog):
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
                # Dati Equipment
                "NumeroEquip": self.ui.lineEdit_NumeroEquip.text(),
                # Dati Indirizzo
                "Via": self.ui.lineEdit_Via.text(),
                "NAP": self.ui.lineEdit_NAP.text(),
                "Comune": self.ui.lineEdit_Comune.text(),
            }
            return data
        except AttributeError as e:
            print(f"Errore: Nomi widget in NuovoEquipmentDialog.py non corretti! {e}")
            return None

