# This Python file uses the following encoding: utf-8
from Include.widgets.ui_giornaliero import Ui_Form
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot, QDateTime
from Include.func.changeColor import changeSVGColor
"""
Aggiungere percentuale completamento
Forse resoconto
(anche i P hanno gli ON)

"""


class GiornalieroWidget(QWidget):
    # Emetterà il NumeroON (ID) del progetto quando il timer parte
    timer_started = Signal(str)
    # Emetterà un dizionario con i dettagli del lavoro quando il timer si ferma
    timer_stopped = Signal(dict)
    def __init__(self, equip="1", np="2", descrizione="Si",progetto_on=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # --- MEMORIZZA I DATI E LO STATO ---
        self.progetto_on = progetto_on  # L'ID univoco del progetto (NumeroON)
        self.is_running = False
        self.start_time = None
        # ----------------------------------
        self.ui.labelDescrizione.setText(descrizione)
        self.ui.labelEquip.setText(equip)
        self.ui.labelNP.setText(np)
        self.ui.pushButtonStart.setIcon(
            changeSVGColor(":/svg/Include/ico/play-circle.svg"))
        self.ui.pushButtonStop.setIcon(
            changeSVGColor(":/svg/Include/ico/stop-circle.svg"))
        self.ui.pushButtonClose.setIcon(
            changeSVGColor(":/svg/Include/ico/x-circle.svg"))
        # --- COLLEGAMENTI E STATO INIZIALE ---
        self.ui.pushButtonStop.setEnabled(False)  # Disabilitato all'inizio
        self.ui.pushButtonStart.clicked.connect(self.start_timer)
        self.ui.pushButtonStop.clicked.connect(self.stop_timer)
        # ------------------------------------

        @Slot()
        def start_timer(self):
            """ Avvia il timer e aggiorna la UI del widget. """
            self.start_time = QDateTime.currentDateTime()
            self.is_running = True

            # Aggiorna UI
            self.ui.pushButtonStart.setEnabled(False)
            self.ui.pushButtonStop.setEnabled(True)
            # (Opzionale) Cambia colore di sfondo per indicare che è attivo
            self.setStyleSheet("background-color: #556B2F;") # Verde scuro

            # Emetti il segnale
            self.timer_started.emit(self.progetto_on)
            print(f"Timer avviato per {self.progetto_on}")

        @Slot()
        def stop_timer(self):
            """ Ferma il timer, calcola la durata e emette i dati. """
            if not self.is_running:
                return

            end_time = QDateTime.currentDateTime()
            self.is_running = False

            # Calcola durata in ore decimali
            duration_seconds = self.start_time.secsTo(end_time)
            duration_hours = duration_seconds / 3600.0  # (es. 1.5 per 1h 30m)
                     # Prepara il pacchetto di dati da inviare
            intervento_data = {
                "progetto_on": self.progetto_on,
                "ora_inizio": self.start_time.toString("HH:mm:ss"),
                "ora_fine": end_time.toString("HH:mm:ss"),
                "ore_lavorate": duration_hours
            }

            # Resetta la UI
            self.ui.pushButtonStart.setEnabled(True)
            self.ui.pushButtonStop.setEnabled(False)
            self.setStyleSheet("") # Rimuovi lo stile di sfondo

            # Emetti il segnale con i dati
            self.timer_stopped.emit(intervento_data)
            print(f"Timer fermato per {self.progetto_on}. Durata: {duration_hours:.2f} ore")
# if __name__ == "__main__":
#     pass
