# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog
from Include.uis.dlgs.ui_NewProjectDialog import Ui_Dialog


class NewProjectDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # --- (Opzionale) Popola i ComboBox ---
                # Per ora usiamo QLineEdit, ma in futuro
                # dovresti caricare qui i clienti e gli equipment
                # self.load_clienti_e_equipment()

    def load_clienti_e_equipment(self):
                # QUI dovresti connetterti al DB e popolare
                # i QComboBox per clienti e equipment
        pass

    def get_data(self):
         """
        Recupera i dati dai campi del dialogo e li
        restituisce come dizionario.

        Presumo i nomi dei widget dal file .ui.
        Sostituiscili con i nomi effettivi.
        """

                # --- USA I NOMI DEI TUOI WIDGET QUI ---
                # Ad esempio, se il tuo .ui usa 'lineEdit_ON' per il NumeroON:

                # Presumo che tu abbia:
                # self.ui.lineEdit_NumeroON
                # self.ui.textEdit_Descrizione
                # self.ui.lineEdit_OreDisponibili
                # self.ui.lineEdit_ClienteID   (Sostituire con ComboBox in futuro)
                # self.ui.lineEdit_Equip        (Sostituire con ComboBox in futuro)

         try:
            data = {
                        "NumeroON": self.ui.lineEdit_NumeroON.text(),
                        "Descrizione": self.ui.textEdit_Descrizione.toPlainText(),
                        "OreDisponibili": self.ui.lineEdit_OreDisponibili.text(),
                        "Cliente_id": self.ui.lineEdit_ClienteID.text(), # Temporaneo
                        "Equip": self.ui.lineEdit_Equip.text()             # Temporaneo
            }
            return data
         except AttributeError as e:
            # Errore comune se i nomi dei widget non corrispondono
            print(f"Errore: Nomi widget in NewProjectDialog.py non corretti! {e}")
            return None
