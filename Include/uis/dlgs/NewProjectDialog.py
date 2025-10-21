# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog
from Include.uis.dlgs.ui_NewProjectDialog import Ui_Dialog


class NewProjectDialog(QDialog):
    STATI_PROGETTO = ["Attivo", "Completato", "In Pausa", "Annullato"]

    def __init__(self, lista_clienti, lista_equipment):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.populate_combos(lista_clienti, lista_equipment)

        self.populate_stato()

        # --- (Opzionale) Popola i ComboBox ---
                # Per ora usiamo QLineEdit, ma in futuro
                # dovresti caricare qui i clienti e gli equipment
                # self.load_clienti_e_equipment()

    def load_clienti_e_equipment(self):
                # QUI dovresti connetterti al DB e popolare
                # i QComboBox per clienti e equipment
        pass

    def populate_stato(self):
        """ Popola il ComboBox dello stato. """
        try:
            self.ui.comboBox_Stato.clear()
            self.ui.comboBox_Stato.addItems(self.STATI_PROGETTO)
            self.ui.comboBox_Stato.setCurrentText("Attivo") # Default
        except AttributeError:
            print("Errore: 'comboBox_Stato' non trovato in NewProjectDialog.ui")

    def populate_combos(self, lista_clienti, lista_equipment):
        """ Popola i menu a tendina con i dati. """

        try:
            self.ui.comboBox_Cliente.clear()
            for cliente_id, nome_display in lista_clienti:
                # Mostra 'nome_display' all'utente
                # Salva 'cliente_id' come dato nascosto
                self.ui.comboBox_Cliente.addItem(nome_display, userData=cliente_id)

            self.ui.comboBox_Equip.clear()
            for equip_id, nome_display in lista_equipment:
                self.ui.comboBox_Equip.addItem(nome_display, userData=equip_id)

        except AttributeError as e:
            print(f"Errore: Nomi ComboBox in NewProjectDialog.py non corretti! {e}")
            #print("Assicurati che si chiamino 'comboBox_Cliente' e 'comboBox_Equip' nel file .ui")

    def get_data(self):
        """
        Recupera i dati dai campi del dialogo, leggendo
        dagli QComboBox invece che dai QLineEdit.
        """
        try:
            data = {
                "NumeroON": self.ui.lineEdit_NumeroON.text(),
                "Descrizione": self.ui.textEdit_Descrizione.toPlainText(),
                "OreDisponibili": self.ui.lineEdit_OreDisponibili.text(),

                # Legge l'ID (userData) salvato nel ComboBox
                "Cliente_id": self.ui.comboBox_Cliente.currentData(),
                "Equip": self.ui.comboBox_Equip.currentData(),
                "Stato": self.ui.comboBox_Stato.currentText()
            }
            return data
        except AttributeError as e:
            print(f"Errore: Nomi widget in NewProjectDialog.get_data non corretti! {e}")
            return None









