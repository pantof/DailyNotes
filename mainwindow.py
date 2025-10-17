# This Python file uses the following encoding: utf-8
import sys
import sqlite3


from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QWidget, QSizePolicy, QListWidgetItem, QMenu, QSystemTrayIcon)
from PySide6.QtGui import QPalette, QIcon, QColor, QAction
from PySide6.QtCore import Slot, QSettings, QByteArray, Qt, QEasingCurve
#from PySide6 import QtCore

from Include.uis.pagine.pagina1 import PaginaHome
from Include.uis.pagine.pagina2 import Pagina2
from Include.uis.pagine.paginaEdit import PaginaEdit
from Include.func.database import createDataBase
from Include.func.changeColor import changeSVGColor
from ui_form import Ui_MainWindow
from Include.uis.Orologio.DisplayOrologio import DisplayOrologio
from Include.widgets.giornaliero import GiornalieroWidget

import rc_risorse

# aggiungere manualmente un orario per un progetto


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.readSettings()
        self.setupWindow()

        self.stackedWidget.insertWidget(0, PaginaHome())
        self.stackedWidget.insertWidget(1, Pagina2())
        pagina_edit = PaginaEdit()
        pagina_edit.progetto_da_salvare.connect(self.save_new_project)
        self.stackedWidget.insertWidget(2, pagina_edit)
        #self.stackedWidget.insertWidget(2, PaginaEdit())
        self.stackedWidget.setCurrentIndex(0)
        self.create_action()
        self.setupToolBar()
        self.defineTransition()

        #Database connection
        self.conn = None
        try:
            self.conn = sqlite3.connect(self.DBName)
            self.conn.row_factory = sqlite3.Row
            createDataBase(self.conn)
        except sqlite3.Error as e:
            print(f"Errore nella connessione al database: {e}")
            QMessageBox.critical(self, "Errore", "Impossibile connettersi al database.")
        finally:
            if self.conn:
                self.conn.close()
        pass

        # serve solo a riempire listwidget
 #       for i in range(5):
 #           print(i)
 #           nuovo_giornaliero = GiornalieroWidget(
 #               f"{i}", f"{i}", f"widget numero {i+1}")
 #           item = QListWidgetItem()
 #           item.setSizeHint(nuovo_giornaliero.sizeHint())
 #           # Impostare l'altezza dell'elemento in base al bottone
 #           self.stackedWidget.widget(1).ui.listWidget.addItem(item)
 #           self.stackedWidget.widget(1).ui.listWidget.setItemWidget(
 #               item, nuovo_giornaliero)
    def loadProgettiIntoPagina2(self):
        """
        Carica i progetti dal database e li inserisce nella listWidget di Pagina2.
        """
        # Ottieni l'istanza della pagina 2
        pagina2 = self.stackedWidget.widget(1)
         # Pulisci la lista da elementi precedenti
        pagina2.ui.listWidget.clear()

        conn = None
        try:
            conn = sqlite3.connect(self.DBName)
            conn.row_factory = sqlite3.Row  # Permette di accedere ai dati per nome colonna
            curs = conn.cursor()

             # Esegui la query per ottenere tutti i progetti
             # Selezioniamo i campi che servono al GiornalieroWidget
            curs.execute("SELECT NumeroON, Descrizione, Equip FROM progetti")
            elenco_progetti = curs.fetchall()

            if not elenco_progetti:
                 # (Opzionale) Qui potresti mostrare un messaggio
                 # in Pagina2 dicendo "Nessun progetto".
                print("Nessun progetto trovato nel database.")
                return

             # Itera sui risultati e popola la lista
            for progetto in elenco_progetti:
                 # Assicurati che i dati non siano None
                equip = progetto["Equip"] if progetto["Equip"] else "N/D"
                np = progetto["NumeroON"] if progetto["NumeroON"] else "N/D"
                descr = progetto["Descrizione"] if progetto["Descrizione"] else "Nessuna descrizione"

                 # Crea il widget personalizzato
                nuovo_giornaliero = GiornalieroWidget(
                    equip=equip,
                    np=np,
                    descrizione=descr,
                    progetto_on=progetto["NumeroON"]  # Passa l'ID del progetto
                )
                # --- COLLEGHIAMO I SEGNALI DEL WIDGET AGLI SLOT DI MAINWINDOW ---
                nuovo_giornaliero.timer_started.connect(self.on_timer_started)
                nuovo_giornaliero.timer_stopped.connect(self.on_timer_stopped)
                # -------------------------------------------------------------

                 # Crea il QListWidgetItem e aggiungilo alla lista
                item = QListWidgetItem()
                item.setSizeHint(nuovo_giornaliero.sizeHint())
                pagina2.ui.listWidget.addItem(item)
                pagina2.ui.listWidget.setItemWidget(item, nuovo_giornaliero)

        except sqlite3.Error as e:
            print(f"Errore nel caricamento dei progetti: {e}")
            QMessageBox.critical(self, "Errore Database",
                                 f"Impossibile caricare i progetti: {e}")
        finally:
            if conn:
                conn.close()

    def defineTransition(self):
        self.stackedWidget.setTransitionDirection(Qt.Vertical)
        self.stackedWidget.setTransitionSpeed(500)
        self.stackedWidget.setTransitionEasingCurve(QEasingCurve.Linear)
        # ACTIVATE Animation
        self.stackedWidget.setSlideTransition(True)

    def setupWindow(self):
        self.setWindowTitle('TEST 1')
        self.setWindowIcon(changeSVGColor(':/svg/Include/ico/calendar.svg'))

    def setupToolBar(self):
        self.spacerWidget = QWidget()
        self.spacerWidget.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)
        # self.mainToolBar.addWidget(Orologio())
        self.mainToolBar.addWidget(DisplayOrologio())
        self.mainToolBar.addAction(self.homeAction)
        self.mainToolBar.addAction(self.pagina2Action)
        self.mainToolBar.addAction(self.paginaEditAction)
        self.mainToolBar.addWidget(self.spacerWidget)
        self.mainToolBar.addAction(self.settings_action)
        self.mainToolBar.addAction(self.about_action)
        self.mainToolBar.addAction(self.about_Qt_action)

    def create_action(self):
        self.homeAction = QAction("&Home", self, triggered=self.setPagina1)
        self.homeAction.setIcon(
            changeSVGColor(":/svg/Include/ico/home.svg"))
        self.pagina2Action = QAction(
            "Pagina&2", self, triggered=self.setPagina2)
        self.pagina2Action.setIcon(
            changeSVGColor(":/svg/Include/ico/menu.svg"))
        self.paginaEditAction = QAction(
            "&Edit", self, triggered=self.setPaginaEdit)
        self.paginaEditAction.setIcon(
            changeSVGColor(":/svg/Include/ico/edit.svg"))
        self.about_action = QAction("&About", self, triggered=self.about)
        self.about_action.setIcon(
            changeSVGColor(":/svg/Include/ico/info.svg"))
        self.settings_action = QAction(
            "&Settings", self, triggered=self.settingsMenu)
        self.settings_action.setIcon(
            changeSVGColor(":/svg/Include/ico/settings.svg"))
        self.about_Qt_action = QAction(
            "About &Qt", self, triggered=qApp.aboutQt)
        self.about_Qt_action.setIcon(QIcon(":/png/Include/ico/qt/qt_logo.png"))

        @Slot(str)
        def on_timer_started(self, progetto_on):
            """
            Slot chiamato quando un timer QUALSIASI parte.
            Qui potresti impedire che altri timer partano.
            """
            print(f"MAINWINDOW: Timer avviato per il progetto {progetto_on}")
            # Per ora, non facciamo nulla, ma potremmo
            # ciclare su tutti i widget e disabilitare gli altri "Start"

        @Slot(dict)
        def on_timer_stopped(self, intervento_data):
            """
            Slot chiamato quando un timer si ferma.
            Qui salviamo i dati nel database.
            """
            print(f"MAINWINDOW: Timer fermato. Dati ricevuti: {intervento_data}")

            # 1. Prendi la data selezionata dal calendario in Pagina1
            pagina1 = self.stackedWidget.widget(0)
            data_selezionata = pagina1.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")

            conn = None
            try:
                conn = sqlite3.connect(self.DBName)
                curs = conn.cursor()

                # 2. Inserisci il nuovo intervento
                sql_insert_intervento = """
                INSERT INTO interventi
                (progetto_on, data_intervento, ora_inizio, ora_fine, ore_lavorate_decimal)
                VALUES (?, ?, ?, ?, ?)
                """
                curs.execute(sql_insert_intervento, (
                    intervento_data["progetto_on"],
                    data_selezionata,
                    intervento_data["ora_inizio"],
                    intervento_data["ora_fine"],
                    intervento_data["ore_lavorate"]
                ))

                    # 3. Aggiorna il totale 'OreUtilizzate' nella tabella 'progetti'
                    # Usiamo CAST e IFNULL per gestire il fatto che la colonna è TEXT
                sql_update_progetto = """
                UPDATE progetti
                SET OreUtilizzate = CAST(IFNULL(OreUtilizzate, '0') AS REAL) + ?
                WHERE NumeroON = ?
                """
                curs.execute(sql_update_progetto, (
                    intervento_data["ore_lavorate"],
                    intervento_data["progetto_on"]
                ))

                conn.commit()
                print("Dati intervento e totale progetto aggiornati con successo.")

            except sqlite3.Error as e:
                print(f"Errore nel salvataggio dell'intervento: {e}")
                QMessageBox.critical(self, "Errore Database",
                                    f"Impossibile salvare l'intervento: {e}")
                if conn:
                    conn.rollback()  # Annulla le modifiche in caso di errore
            finally:
                if conn:
                    conn.close()

    @Slot()
    def about(self):
        QMessageBox.about(
                        self, "Dayly Note",
                        "<b> &copy; 2023 Filippo De Filippis</b>"
                        "<br/>The <b>Dayly Note</b> "
                        "Ricordati di chiudere il programma dal tray")

    @Slot()
    def setPagina1(self):
        self.stackedWidget.slideToWidgetIndex(0)
        # self.stackedWidget.setCurrentIndex(0)

    @Slot()
    def setPagina2(self):
        self.loadProgettiIntoPagina2()  # <--
        self.stackedWidget.slideToWidgetIndex(1)
        # self.stackedWidget.setCurrentIndex(1)

    @Slot()
    def setPaginaEdit(self):
        self.stackedWidget.slideToWidgetIndex(2)

    @Slot()
    def settingsMenu(self):
        pass

    def writeSettings(self):
        settings = QSettings("TEST")
        settings.beginGroup("Main Window")
        settings.setValue("geometry", self.saveGeometry())
        settings.endGroup()
        settings.beginGroup("Database")
        if self.DBName == "":
            settings.setValue("DatabaseName", "DefaultName.pntf")
        else:
            settings.setValue("DatabaseName", self.DBName)
        settings.endGroup()

    def readSettings(self):
        settings = QSettings("TEST")
        settings.beginGroup("Main Window")
        geometry = settings.value("geometry", QByteArray())
        if geometry.isEmpty():
            self.setGeometry(200, 200, 400, 400)
        else:
            self.restoreGeometry(geometry)
        settings.endGroup()
        settings.beginGroup("Database")
        self.DBName = str(settings.value("DatabaseName", str()))
        if self.DBName == "":
            self.DBName = "DefaultName.pntf"

    @Slot()
    def activate(self, reason):
        if reason == QSystemTrayIcon.Trigger:  # Icon clicked.
            if reason == QSystemTrayIcon.Trigger:
                if self.isVisible():
                    self.hide()
                else:
                    self.show()

    @Slot(dict)
    def save_new_project(self, data):
        """
        Slot che riceve i dati da PaginaEdit e li salva nel database.
        """
        print(f"MAINWINDOW: Salvataggio nuovo progetto: {data}")

        conn = None
        try:
            conn = sqlite3.connect(self.DBName)
            curs = conn.cursor()

            # La tabella progetti ha 6 colonne:
            # NumeroON, Descrizione, OreDisponibili, OreUtilizzate, Cliente_id, Equip
            sql_insert_progetto = """
                                INSERT INTO progetti
                                    (NumeroON, Descrizione, OreDisponibili, OreUtilizzate, Cliente_id, Equip)
                                VALUES (?, ?, ?, ?, ?, ?)
                                """

            # OreUtilizzate è 0 all'inizio.
            # Convertiamo OreDisponibili in testo (come da schema)
            ore_disp_text = str(data["OreDisponibili"]) if data["OreDisponibili"] else "0"

            curs.execute(sql_insert_progetto, (
                                    data["NumeroON"],
                                    data["Descrizione"],
                                    ore_disp_text,
                                    "0",  # OreUtilizzate
                                    data["Cliente_id"], # Temporaneamente un testo
                                    data["Equip"]       # Temporaneamente un testo
                                ))

            conn.commit()
            print("Nuovo progetto salvato con successo.")

            # Opzionale: aggiorna la lista in Pagina2 se è già stata caricata
            # self.loadProgettiIntoPagina2()

        except sqlite3.IntegrityError as e:
            # Errore comune se il NumeroON è già presente (PRIMARY KEY)
            print(f"Errore di integrità: {e}")
            QMessageBox.critical(self, "Errore Database",
                                                     f"Impossibile salvare il progetto:\n"
                                                     f"Il Numero ON '{data['NumeroON']}' esiste già.")
        except sqlite3.Error as e:
            print(f"Errore nel salvataggio del progetto: {e}")
            QMessageBox.critical(self, "Errore Database",
                                                     f"Impossibile salvare il progetto: {e}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                conn.close()

    @Slot()
    def activateFromMenu(self):
        self.show()

    def save(self):
        pass

    def closeEvent(self, event):
        # print("Close Event")
        self.writeSettings()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setQuitOnLastWindowClosed(False)
    icon = changeSVGColor(":/svg/Include/ico/calendar.svg")
    widget = MainWindow()
    widget.setWindowIcon(icon)
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(60, 60, 60))
    palette.setColor(QPalette.Button, QColor(50, 50, 50))
    palette.setColor(QPalette.Base, QColor(100, 100, 100))
    palette.setColor(QPalette.AlternateBase, QColor(120, 120, 120))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.Highlight, QColor(150, 150, 150))
    app.setPalette(palette)
    widget.show()
    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    menu = QMenu()
    action = QAction("Visualizza")
    action.triggered.connect(widget.activateFromMenu)
    menu.addAction(action)
    # Add a Quit option to the menu.
    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)
    tray.setContextMenu(menu)
    tray.activated.connect(widget.activate)
    app.aboutToQuit.connect(widget.save)
    sys.exit(app.exec())
