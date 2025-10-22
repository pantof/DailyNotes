# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem,
                               QPushButton, QHBoxLayout, QHeaderView, QMessageBox,
                               QAbstractItemView)
from PySide6.QtCore import Signal, Slot, Qt

class GestioneProgettiDialog(QDialog):
    """
    Dialogo per visualizzare, modificare (stato) ed eliminare progetti.
    """
    # Segnale emesso con (NumeroON, nuovo_stato)
    progetto_stato_changed = Signal(str, str)
    # Segnale emesso con (NumeroON)
    progetto_da_eliminare = Signal(str)

    def __init__(self, db_name, parent=None):
        super().__init__(parent)
        self.db_name = db_name
        self.setWindowTitle("Gestione Progetti")
        self.setMinimumSize(700, 400) # Imposta una dimensione minima

        # Layout
        layout = QVBoxLayout(self)

        # Tabella
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5) # NumeroON, Descrizione, Cliente, Ore, Stato
        self.tableWidget.setHorizontalHeaderLabels(["Numero ON", "Descrizione", "Cliente", "Ore Utilizzate", "Stato"])
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) # Non editabile
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows) # Seleziona riga intera
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection) # Solo una riga
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents) # Descrizione

        layout.addWidget(self.tableWidget)

        # Layout Pulsanti
        button_layout = QHBoxLayout()
        self.modificaStatoButton = QPushButton("Modifica Stato")
        self.eliminaProgettoButton = QPushButton("Elimina Progetto")

        button_layout.addStretch()
        button_layout.addWidget(self.modificaStatoButton)
        button_layout.addWidget(self.eliminaProgettoButton)
        layout.addLayout(button_layout)

        # Connessioni
        self.modificaStatoButton.clicked.connect(self.on_modifica_stato)
        self.eliminaProgettoButton.clicked.connect(self.on_elimina_progetto)

        # Carica i dati
        self.carica_progetti()

    def carica_progetti(self):
        """ Carica tutti i progetti dal DB e popola la tabella. """
        import sqlite3
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()

            # Query per ottenere tutti i progetti e il nome del cliente
            sql = """
            SELECT P.*, C.Azienda, C.Nome, C.Cognome
            FROM progetti P
            LEFT JOIN clienti C ON P.Cliente_id = C.rowid
            ORDER BY P.NumeroON
            """
            curs.execute(sql)
            progetti = curs.fetchall()

            self.tableWidget.setRowCount(len(progetti))
            for row_idx, progetto in enumerate(progetti):
                # Costruisci nome cliente
                if progetto["Azienda"]:
                    nome_cliente = progetto["Azienda"]
                elif progetto["Cognome"]:
                    nome_cliente = f"{progetto['Cognome']} {progetto['Nome']}"
                else:
                    nome_cliente = "N/D"

                # Crea items
                item_on = QTableWidgetItem(progetto["NumeroON"])
                item_descr = QTableWidgetItem(progetto["Descrizione"])
                item_cliente = QTableWidgetItem(nome_cliente)
                item_ore = QTableWidgetItem(f"{float(progetto['OreUtilizzate'] or 0):.2f}")
                item_stato = QTableWidgetItem(progetto["Stato"])

                # Imposta gli items nella tabella
                self.tableWidget.setItem(row_idx, 0, item_on)
                self.tableWidget.setItem(row_idx, 1, item_descr)
                self.tableWidget.setItem(row_idx, 2, item_cliente)
                self.tableWidget.setItem(row_idx, 3, item_ore)
                self.tableWidget.setItem(row_idx, 4, item_stato)

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Errore Database", f"Impossibile caricare i progetti: {e}")
        finally:
            if conn:
                conn.close()

    def get_selected_project_on(self):
        """ Ritorna il NumeroON della riga selezionata, o None. """
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Attenzione", "Nessun progetto selezionato.")
            return None
        # L'item 0 (NumeroON) della riga selezionata
        return selected_items[0].text()

    @Slot()
    def on_modifica_stato(self):
        """ Chiede un nuovo stato ed emette un segnale. """
        progetto_on = self.get_selected_project_on()
        if not progetto_on:
            return

        # Semplice QInputDialog per chiedere il nuovo stato
        # (Usa gli stessi stati del NewProjectDialog)
        from PySide6.QtWidgets import QInputDialog
        stati = ["Attivo", "Completato", "In Pausa", "Annullato"]
        nuovo_stato, ok = QInputDialog.getItem(self, "Modifica Stato",
                                             f"Seleziona un nuovo stato per {progetto_on}:",
                                             stati, 0, False)

        if ok and nuovo_stato:
            self.progetto_stato_changed.emit(progetto_on, nuovo_stato)
            # Ricarica la tabella per mostrare la modifica
            self.carica_progetti()

    @Slot()
    def on_elimina_progetto(self):
        """ Chiede conferma ed emette un segnale. """
        progetto_on = self.get_selected_project_on()
        if not progetto_on:
            return

        reply = QMessageBox.question(self, "Conferma Eliminazione",
                                     f"Sei sicuro di voler eliminare il progetto {progetto_on}?\n"
                                     "ATTENZIONE: Verranno eliminati anche tutti gli interventi associati!",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.progetto_da_eliminare.emit(progetto_on)
            # Ricarica la tabella
            self.carica_progetti()


# if __name__ == "__main__":
#     pass
