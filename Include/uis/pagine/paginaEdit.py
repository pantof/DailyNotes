# This Python file uses the following encoding: utf-8
import sqlite3
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from Include.uis.pagine.ui_paginaEdit import Ui_paginaEdit
from Include.uis.dlgs.NewProjectDialog import NewProjectDialog
from Include.uis.dlgs.NuovoClienteDialog import NuovoClienteDialog
from Include.uis.dlgs.NuovoEquipmentDialog import NuovoEquipmentDialog
from Include.func.changeColor import changeSVGColor
from Include.uis.dlgs.GestioneProgettiDialog import GestioneProgettiDialog

class PaginaEdit(QWidget):
    progetto_da_salvare = Signal(dict)
    cliente_da_salvare = Signal(dict)
    equipment_da_salvare = Signal(dict)
    progetto_stato_da_aggiornare = Signal(str, str)
    #progetto_da_eliminare_definitivo = Signal(str)
    progetto_da_archiviare = Signal(str)

    def __init__(self,db_name):
        super().__init__()
        self.ui = Ui_paginaEdit()
        self.ui.setupUi(self)
        self.db_name = db_name

        self.ui.pushButton_1.clicked.connect(self.lanciaNewProject)
        self.ui.pushButton_2.clicked.connect(self.lanciaNuovoCliente)
        self.ui.pushButton_3.clicked.connect(self.NuovoEquipment)
        try:
            self.ui.gestisciProgettiButton.clicked.connect(self.lanciaGestioneProgetti)
        except AttributeError:
            print("Errore: 'gestisciProgettiButton' non trovato in paginaEdit.ui")

    def lanciaNewProject(self):
        lista_clienti = self.fetch_clienti()
        lista_equipment = self.fetch_equipment()
        if not lista_clienti or not lista_equipment:
            QMessageBox.warning(self, "Dati mancanti",
                                            "Impossibile creare un progetto.\n"
                                            "Assicurati di aver inserito almeno un cliente e un equipment.")
            return

        newProject = NewProjectDialog(lista_clienti, lista_equipment)
        newProject.setWindowTitle("Nuovo Progetto")
        newProject.setWindowIcon(
            changeSVGColor(":/svg/Include/ico/edit-3.svg"))
        if newProject.exec():
            data =newProject.get_data()
            if not data:
                QMessageBox.critical(self, "Errore", "Errore nel recupero dati dal dialogo.")
                return
            if not data["NumeroON"] or not data["Descrizione"]:
                QMessageBox.warning(self, "Dati Mancanti",
                                    "Numero ON e Descrizione sono obbligatori.")
                return

            self.progetto_da_salvare.emit(data)
            QMessageBox.information(self, "Successo",
                                    f"Progetto {data['NumeroON']} salvato.")
            #print("salva")  # controllo inserimento dati
        else:
            print("Creazione progetto annullata")

    def lanciaNuovoCliente(self):
        """ Lancia il dialogo Nuovo Cliente ed emette il segnale per salvarlo. """
        newCliente = NuovoClienteDialog()
        newCliente.setWindowTitle("Nuovo Cliente")
        newCliente.setWindowIcon(changeSVGColor(":/svg/Include/ico/user-plus.svg"))
        if newCliente.exec():
            data = newCliente.get_data()
            if not data:
                QMessageBox.critical(self, "Errore", "Errore nei nomi dei widget del dialogo.")
                return
            # Validazione: Azienda o Nome/Cognome obbligatori
            if not data["Azienda"] and (not data["Nome"] or not data["Cognome"]):
                QMessageBox.warning(self, "Dati Mancanti","È necessario inserire 'Azienda' o 'Nome' e 'Cognome'.")
                return
            # Emetti segnale
            self.cliente_da_salvare.emit(data)
            QMessageBox.information(self, "Successo", "Nuovo cliente salvato.")



    def NuovoEquipment(self):
        """ Lancia il dialogo Nuovo Equipment ed emette il segnale per salvarlo. """
        newEquip = NuovoEquipmentDialog()
        newEquip.setWindowTitle("Nuovo Equipment")
        newEquip.setWindowIcon(changeSVGColor(":/svg/Include/ico/tool.svg"))

        if newEquip.exec():
            data = newEquip.get_data()
            if not data:
                QMessageBox.critical(self, "Errore", "Errore nei nomi dei widget del dialogo.")
                return
            if not data["NumeroEquip"]:
                QMessageBox.warning(self, "Dati Mancanti","Il 'Numero Equipment' è obbligatorio.")
                return
            # Emetti segnale
            self.equipment_da_salvare.emit(data)
            QMessageBox.information(self, "Successo", "Nuovo equipment salvato.")


    def controlloInserimentoDati(self):
        pass
    def fetch_clienti(self):
        """ Carica i clienti dal DB per il ComboBox. """
        clienti = []
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            # Selezioniamo 'rowid' (l'ID univoco) e un nome da mostrare
            curs.execute("SELECT rowid, Azienda, Nome, Cognome FROM clienti ORDER BY Azienda, Cognome")
            for row in curs.fetchall():
                nome_display = row["Azienda"] if row["Azienda"] else f"{row['Cognome']} {row['Nome']}"
                clienti.append((row["rowid"], nome_display))
            return clienti
        except sqlite3.Error as e:
            print(f"Errore fetch_clienti: {e}")
            return [] # Ritorna lista vuota in caso di errore
        finally:
            if conn:
                conn.close()

    def fetch_equipment(self):
        """ Carica gli equipment dal DB per il ComboBox. """
        equipment = []
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
                        # Selezioniamo 'NumeroEquip' (Primary Key)
            curs.execute("SELECT NumeroEquip FROM equipment ORDER BY NumeroEquip")
            for row in curs.fetchall():
                equipment.append((row["NumeroEquip"], row["NumeroEquip"]))
            return equipment
        except sqlite3.Error as e:
            print(f"Errore fetch_equipment: {e}")
            return []
        finally:
            if conn:
                conn.close()

    @Slot()
    def lanciaGestioneProgetti(self):
        """ Apre il dialogo di gestione progetti e connette i suoi segnali. """
        dialog = GestioneProgettiDialog(self.db_name, self)

        # Collega i segnali del dialogo ai segnali di PaginaEdit
        # (che a loro volta saranno connessi a MainWindow)
        dialog.progetto_stato_changed.connect(self.progetto_stato_da_aggiornare)
        #dialog.progetto_da_eliminare.connect(self.progetto_da_eliminare_definitivo)
        dialog.progetto_da_archiviare.connect(self.progetto_da_archiviare)

        dialog.exec()
