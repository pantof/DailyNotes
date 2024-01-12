# This Python file uses the following encoding: utf-8


class TabellaProgetti:
    def __init__(self, connection):
        self.connessione = connection
        self.cursore = connection.cursor()
        self.listaEntity = []
        self.listaEntityFromDB = []
        pass

    def buildDictListProgetti(self):
        pass

    def writeDictListToDB(self):
        pass

    def getDictListToDB(self, nomeTabella):
        pass
