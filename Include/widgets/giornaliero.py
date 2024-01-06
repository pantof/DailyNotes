# This Python file uses the following encoding: utf-8
from Include.widgets.ui_giornaliero import Ui_Form
from PySide6.QtWidgets import QWidget
from Include.func.changeColor import changeSVGColor


class GiornalieroWidget(QWidget):
    def __init__(self, equip="1", np="2", descrizione="Si"):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.labelDescrizione.setText(descrizione)
        self.ui.labelEquip.setText(equip)
        self.ui.labelNP.setText(np)
        self.ui.pushButtonStart.setIcon(
            changeSVGColor(":/svg/Include/ico/play-circle.svg"))
        self.ui.pushButtonStop.setIcon(
            changeSVGColor(":/svg/Include/ico/stop-circle.svg"))
        self.ui.pushButtonClose.setIcon(
            changeSVGColor(":/svg/Include/ico/x-circle.svg"))

# if __name__ == "__main__":
#     pass
