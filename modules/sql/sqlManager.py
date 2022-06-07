import sqlite3
from log.Log import Log
from calculos.distanciaPercorridaSatelite import calcularDistanciaPercorrida
conectarDB_Satelite = sqlite3.connect("SateliteISS.db")

cursorSatelite = conectarDB_Satelite.cursor()

cursorSatelite.execute("""
                       CREATE TABLE IF NOT EXISTS SateliteLog(
                           ID: INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                           DATAHORA: DATETIME NOT NULL
                           LATITUDE: REAL NOT NULL,
                           LONGITUDE: REAL NOT NULL,
                           
                       )
                       """)



def inserirNovoLog(log):
    
    cursorSatelite.execute("""
                                    SELECT * FROM SateliteLog ORDER by ID DESC LIMIT 1;
                           """)
    lastLog = cursorSatelite.fetchone()
    distPercorrida = calcularDistanciaPercorrida(lastLog[2],log.lat,lastLog[3],log.l)
    new_log = Log(log.dataHora,log.lat,log.long,distPercorrida)
    cursorSatelite.execute("""
                                    
                                    INSERT INTO SateliteLog(DATAHORA,LATITUDE,LONGITUDE) values (?,?,?);
                                    
                                    
                                    """,
                                    (new_log.datahora,new_log.lat,new_log.lng,new_log.distanciaPercorrida)
    )
        
    conectarDB_Satelite.commit()
    return


