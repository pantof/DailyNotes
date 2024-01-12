# This Python file uses the following encoding: utf-8


class TabellaIndirizzi:
    def __init__(self, connection):
        self.connessione = connection
        self.cursore = connection.cursor()
        self.listaEntity = []
        self.listaEntityFromDB = []
        pass

    def buildDictListIndirizzi(self):
        pass
