import math
from sql.sqlManager import cursorSatelite

cursorSatelite.execute("""
                        
                        SELECT * FROM SateliteLog 
                        
                       """)

def variacaoAltitude():
    array = cursorSatelite.fetchall()
    som = 0
    
    for log in array:
        som += log[4]
        
    media = som / len(array)
    sigma = 0 
    
    for val in array:
        sigma += (val[4] - media) ** 2 
     
       
    desvio_padrao =  math.sqrt( sigma / len(array) )
    return desvio_padrao