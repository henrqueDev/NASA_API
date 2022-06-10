import math
import mpmath
from sql.sqlManager import cursorSatelite


cursorSatelite.execute("""
                        
                        SELECT * FROM SateliteLog 
                        
                       """)

def varianciaAltitude():
    return