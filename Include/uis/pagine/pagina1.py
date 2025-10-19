# This Python file uses the following encoding: utf-8
# import sys
import sqlite3
from collections import defaultdict
from PySide6.QtWidgets import QWidget, QListWidgetItem, QLabel
from PySide6.QtCore import Slot, QDate, Qt, Signal
from PySide6.QtGui import QTextCharFormat, QColor, QBrush, QPalette
# from PySide6 import Qt
# void QCalendarWidget::setCurrentPage(int year, int month)

from Include.uis.pagine.ui_pagina1 import Ui_Pagina01
from Include.widgets.RiepilogoItemWidget import RiepilogoItemWidget
from Include.func.changeColor import changeSVGColor
from Include.widgets.RiepilogoProgettoWidget import RiepilogoProgettoWidget
from Include.widgets.RiepilogoInterventoWidget import RiepilogoInterventoWidget
from Include.uis.dlgs.ManualeInterventoDialog import ManualeInterventoDialog
"""
https://stackoverflow.com/questions/60659643/how-to-change-the-background-colour-of-a-cell-in-a-qcalendarwidget-using-an-sql
https://stackoverflow.com/questions/56253427/coloring-pyqt5-qcalendarwidget-cell-and-printing-data-inside-the-cells?noredirect=1&lq=1
https://stackoverflow.com/questions/58165586/highlight-date-interval-in-a-qt5-calendar-widget?noredirect=1&lq=1

"""


class PaginaHome(QWidget):
    intervento_manuale_da_salvare = Signal(dict)
    def __init__(self, db_name):
        super().__init__()
        self.ui = Ui_Pagina01()
        # self.widgetOrologio. = Orologio()
        self.ui.setupUi(self)
        self.db_name = db_name
        self.now = QDate.currentDate()
        self.ui.spinBoxAnno.setValue(self.now.year())
        self.ui.mesi.setCurrentIndex(self.now.month()-1)
        self.ui.labelData.setText(self.now.toString("dd.MM.yyyy"))
        # print(self.now.month()-1)
        calendarPalette = QPalette()
        calendarPalette.setColor(QPalette.Text, QColor(255, 255, 255))
        self.sundayFormat = QTextCharFormat()
        # calendarPalette.setColor(
        # self.saturdayFormat = QTextCharFormat()
        self.sundayFormat.setForeground(QBrush(QColor("cyan")))
        self.ui.calendarWidget.setWeekdayTextFormat(
            Qt.DayOfWeek.Sunday, self.sundayFormat)
        self.ui.calendarWidget.setWeekdayTextFormat(
            Qt.DayOfWeek.Saturday, self.sundayFormat)
        # self.ui.calendarWidget.setba
        self.ui.calendarWidget.setPalette(calendarPalette)

        self.ui.nextMonth.setIcon(
            changeSVGColor(":/svg/Include/ico/arrow-right.svg"))
        self.ui.prevMonth.setIcon(
            changeSVGColor(":/svg/Include/ico/arrow-left.svg"))
        self.ui.mesi.currentIndexChanged.connect(self.meseCambiato)
        self.ui.calendarWidget.currentPageChanged.connect(
            self.dataCambiataDaCalendario)
        self.ui.calendarWidget.selectionChanged.connect(
            self.cambioSelezioneCalendario)
        self.ui.spinBoxAnno.valueChanged.connect(self.cambioDataDaSpinBox)
        try:
            self.ui.listWidget_Riepilogo.itemClicked.connect(self.on_riepilogo_item_clicked)
        except AttributeError:
            print("Errore: 'listWidget_Riepilogo' non trovato.")

        self.carica_riepilogo_giornaliero()
    @Slot()
    def refresh_data(self):
        """ Slot pubblico per forzare l'aggiornamento del riepilogo. """
        self.carica_riepilogo_giornaliero()

    @Slot()
    def meseCambiato(self):
        # Cambio mese da combo a Calendario
        # print(self.ui.mesi.currentText())
        # print(self.ui.mesi.currentIndex()+1)
        self.ui.calendarWidget.setCurrentPage(
            self.ui.spinBoxAnno.value(), self.ui.mesi.currentIndex()+1)

    @Slot()
    def dataCambiataDaCalendario(self):
        self.ui.mesi.setCurrentIndex(self.ui.calendarWidget.monthShown()-1)
        self.ui.spinBoxAnno.setValue(self.ui.calendarWidget.yearShown())
        self.ui.labelData.setText(
            self.ui.calendarWidget.selectedDate().toString("dd.MM.yyyy"))
        # Cambio data da calendario a combo

    @Slot()
    def cambioDataDaSpinBox(self):
        self.ui.calendarWidget.setCurrentPage(
            self.ui.spinBoxAnno.value(), self.ui.mesi.currentIndex()+1)

    @Slot()
    def cambioSelezioneCalendario(self):
        self.ui.labelData.setText(
            self.ui.calendarWidget.selectedDate().toString("dd.MM.yyyy"))
        self.carica_riepilogo_giornaliero()

    def carica_riepilogo_giornaliero(self):
        """
        Carica gli interventi dal DB per la data selezionata
        e li mostra nel listWidget_Riepilogo.
        """
        try:
            self.ui.listWidget_Riepilogo.clear()
        except AttributeError:
            # Errore se il listWidget_Riepilogo non è stato aggiunto in Designer
            print("Errore: 'listWidget_Riepilogo' non trovato in pagina1.ui")
            return

        data_selezionata = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        item_totale_giornata = QListWidgetItem()
        label_totale_giornata = QLabel("TOTALE GIORNATA: 0.00 ore")
        label_totale_giornata.setStyleSheet("font-weight: bold; font-size: 11pt; padding: 3px;")
        self.ui.listWidget_Riepilogo.addItem(item_totale_giornata)
        self.ui.listWidget_Riepilogo.setItemWidget(item_totale_giornata, label_totale_giornata)

        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()

            sql = """
            SELECT
                            P.Descrizione, P.NumeroON,
                            I.ore_lavorate_decimal, I.ora_inizio, I.ora_fine,
                            C.Azienda, C.Nome, C.Cognome
                        FROM interventi I
                        JOIN progetti P ON I.progetto_on = P.NumeroON
                        LEFT JOIN clienti C ON P.Cliente_id = C.rowid
                        WHERE I.data_intervento = ?
                        ORDER BY I.ora_inizio
                """
            curs.execute(sql, (data_selezionata,))
            interventi = curs.fetchall()

            if not interventi:
                QListWidgetItem("Nessun intervento registrato.", self.ui.listWidget_Riepilogo)
                label_totale_giornata.setText("TOTALE GIORNATA: 0.00 ore")
                return

            ore_giornata_totali = 0.0
            progetti_del_giorno = defaultdict(lambda: {
                            "info": {},
                            "interventi": [],
                            "ore_totali_progetto": 0.0
            })
            for row in interventi:
                pid = row["NumeroON"]
                ore_intervento = row["ore_lavorate_decimal"]
                ore_giornata_totali += ore_intervento
                progetti_del_giorno[pid]["info"] = row
                progetti_del_giorno[pid]["interventi"].append(row)
                progetti_del_giorno[pid]["ore_totali_progetto"] += ore_intervento

            for progetto_on, gruppo in progetti_del_giorno.items():
                info = gruppo["info"]
                ore_progetto = gruppo["ore_totali_progetto"]

                if info["Azienda"]:
                    nome_cliente = info["Azienda"]
                elif info["Cognome"]:
                    nome_cliente = f"{info['Cognome']} {info['Nome']}"
                else:
                    nome_cliente = "N/D"

                # --- Aggiungi l'intestazione del progetto ---
                widget_header = RiepilogoProgettoWidget(progetto_on, nome_cliente, ore_progetto)
                item_header = QListWidgetItem()
                item_header.setSizeHint(widget_header.sizeHint())
                self.ui.listWidget_Riepilogo.addItem(item_header)
                self.ui.listWidget_Riepilogo.setItemWidget(item_header, widget_header)




                for intervento in gruppo["interventi"]:
                    widget_intervento = RiepilogoInterventoWidget(
                                        intervento["Descrizione"],
                                        intervento["ora_inizio"],
                                        intervento["ora_fine"],
                                        intervento["ore_lavorate_decimal"]
                    )
                    item_intervento = QListWidgetItem()
                    item_intervento.setSizeHint(widget_intervento.sizeHint())
                    self.ui.listWidget_Riepilogo.addItem(item_intervento)
                    self.ui.listWidget_Riepilogo.setItemWidget(item_intervento, widget_intervento)
            label_totale_giornata.setText(f"TOTALE GIORNATA: {ore_giornata_totali:.2f} ore")



        except sqlite3.Error as e:
            print(f"Errore carica_riepilogo_giornaliero: {e}")
            QListWidgetItem(f"Errore DB: {e}", self.ui.listWidget_Riepilogo)
        finally:
            if conn:
                conn.close()

    @Slot(QListWidgetItem)
    def on_riepilogo_item_clicked(self, item):
        """ Chiamato quando l'utente clicca un item nel riepilogo. """

        widget = self.ui.listWidget_Riepilogo.itemWidget(item)

        # Controlla se abbiamo cliccato un'intestazione di progetto
        if isinstance(widget, RiepilogoProgettoWidget):
            # Recupera i dati che abbiamo salvato nel widget
            progetto_on = widget.progetto_on
            nome_cliente = widget.nome_cliente
            data_selezionata = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")

            # Lancia il dialogo
            dialog = ManualeInterventoDialog(progetto_on, nome_cliente, data_selezionata, self)

            if dialog.exec():
                ore_inserite = dialog.get_ore()

                if ore_inserite > 0:
                    # Prepara il pacchetto di dati da inviare a MainWindow
                    dati_intervento = {
                        "progetto_on": progetto_on,
                        "data_intervento": data_selezionata,
                        "ore_lavorate": ore_inserite
                    }
                    # Emetti il segnale
                    self.intervento_manuale_da_salvare.emit(dati_intervento)



if __name__ == "__main__":
    pass
