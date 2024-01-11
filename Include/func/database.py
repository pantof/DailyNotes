# This Python file uses the following encoding: utf-8
# import sqlite3


def createDataBase(connection):

    curs = connection.cursor()
    try:
        # 2. Imposta la password
        # password = "HmgUqvVY8Ceb3zuWjRTw4yckMBJnF2ArDP9tNQf5pshd7LZXxE"
        # connection.execute(f"PRAGMA key='{password}'")
        curs.execute("PRAGMA foreign_keys = ON;")
        curs.execute("CREATE TABLE IF NOT EXISTS clienti("
                     "Azienda TEXT, "
                     "Nome TEXT, "
                     "Cognome TEXT, "
                     "indirizzo_id INTEGER, "
                     "FOREIGN KEY(indirizzo_id) REFERENCES indirizzi(rowid));")
        curs.execute("CREATE TABLE IF NOT EXISTS indirizzi("
                     "Via TEXT, "
                     "NAP TEXT, "
                     "Comune TEXT);")
        curs.execute("CREATE TABLE IF NOT EXISTS equipment("
                     "NumeroEquip TEXT, "
                     "indirizzo_id INTEGER, "
                     "PRIMARY KEY(NumeroEquip) ON CONFLICT REPLACE, "
                     "FOREIGN KEY(indirizzo_id) REFERENCES indirizzi(rowid));")
        curs.execute("CREATE TABLE IF NOT EXISTS progetti("
                     "NumeroON TEXT, "
                     "Descrizione TEXT, "
                     "OreDisponibili TEXT, "
                     "OreUtilizzate TEXT, "
                     "Cliente_id INTEGER, "
                     "Equip TEXT, "
                     "PRIMARY KEY(NumeroON) ON CONFLICT REPLACE,"
                     "FOREIGN KEY(Cliente_id) REFERENCES clienti(rowid), "
                     "FOREIGN KEY(Equip) REFERENCES equipment(NumeroEquip));")
        connection.commit()
    except Exception as e:
        print(f"Errore: {e}")
        return None
    finally:
        # Chiudi la connessione
        curs.close()

# if __name__ == "__main__":
#     pass
