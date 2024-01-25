# This Python file uses the following encoding: utf-8
import sys
import sqlite3


from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QWidget, QSizePolicy, QListWidgetItem, QMenu, QSystemTrayIcon)
from PySide6.QtGui import QPalette, QIcon, QColor, QAction
# , QPixmap, QPainter
from PySide6.QtCore import Slot, QSettings, QByteArray
from PySide6 import QtCore

from Include.uis.pagine.pagina1 import PaginaHome
from Include.uis.pagine.pagina2 import Pagina2
from Include.uis.pagine.paginaEdit import PaginaEdit
from Include.func.database import createDataBase
from Include.func.changeColor import changeSVGColor
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
# from Include.uis.LCDclock.LCDclock import Orologio
from Include.uis.Orologio.DisplayOrologio import DisplayOrologio
from Include.widgets.giornaliero import GiornalieroWidget
# from Include.widgets.custom import CustomQStackedWidget
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
        self.stackedWidget.insertWidget(2, PaginaEdit())
        self.stackedWidget.setCurrentIndex(0)
        self.create_action()
        self.setupToolBar()
        self.defineTransition()
        self.conn = sqlite3.connect(self.DBName)
        self.curs = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row
        createDataBase(self.conn)
        # serve solo a riempire listwidget
        for i in range(5):
            print(i)
            nuovo_giornaliero = GiornalieroWidget(
                f"{i}", f"{i}", f"widget numero {i+1}")
            item = QListWidgetItem()
            item.setSizeHint(nuovo_giornaliero.sizeHint())
# Impostare l'altezza dell'elemento in base al bottone
            self.stackedWidget.widget(1).ui.listWidget.addItem(item)
            self.stackedWidget.widget(1).ui.listWidget.setItemWidget(
                item, nuovo_giornaliero)

    def defineTransition(self):
        self.stackedWidget.setTransitionDirection(QtCore.Qt.Vertical)
        self.stackedWidget.setTransitionSpeed(500)
        self.stackedWidget.setTransitionEasingCurve(QtCore.QEasingCurve.Linear)
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
