# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal
from Include.uis.pagine.ui_paginaEdit import Ui_paginaEdit
from Include.uis.dlgs.NewProjectDialog import NewProjectDialog
from Include.uis.dlgs.NuovoClienteDialog import NuovoClienteDialog
from Include.uis.dlgs.NuovoEquipmentDialog import NuovoEquipmentDialog
from Include.func.changeColor import changeSVGColor


class PaginaEdit(QWidget):
    progetto_da_salvare = Signal(dict)
    cliente_da_salvare = Signal(dict)
    equipment_da_salvare = Signal(dict)

    def __init__(self):
        super().__init__()
        self.ui = Ui_paginaEdit()
        # self.widgetOrologio. = Orologio()
        self.ui.setupUi(self)
        self.ui.pushButton_1.clicked.connect(self.lanciaNewProject)
        self.ui.pushButton_2.clicked.connect(self.lanciaNuovoCliente)
        self.ui.pushButton_3.clicked.connect(self.NuovoEquipment)

    def lanciaNewProject(self):
        newProject = NewProjectDialog()
        newProject.setWindowTitle("Nuovo Progetto")
        newProject.setWindowIcon(
            changeSVGColor(":/svg/Include/ico/edit-3.svg"))
        if newProject.exec():
            data =newProject.get_data()
            if not data:
                QMessageBox.critical(self, "Errore", "Errore nei nomi dei widget del dialogo.")
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

