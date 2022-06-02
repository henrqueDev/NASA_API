import sqlite3


conectarDB_Satelite = sqlite3.connect("SateliteISS.db")

cursorSatelite = conectarDB_Satelite.cursor()

cursorSatelite.execute("""
                       CREATE TABLE IF NOT EXISTS SateliteLog(
                           ID: INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                           DATAHORA: DATETIME NOT NULL
                           LATITUDE: REAL NOT NULL,
                           LONGITUDE: REAL NOT NULL
                       )
                       """)



def inserirNovoLog(log):
    
    newLog = cursorSatelite.execute(f"""
                                    
                                    INSERT INTO SateliteLog(DATAHORA,LATITUDE,LONGITUDE) values (?,?,?)
                                    
                                    
                                    """,
                                    (log.datahora,log.lat,log.lng)
    )
    
    return
