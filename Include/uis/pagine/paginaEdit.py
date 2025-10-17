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
        pass

    def NuovoEquipment(self):
        pass

    def controlloInserimentoDati(self):
        pass

