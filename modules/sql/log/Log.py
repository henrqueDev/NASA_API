class Log:
    def __init__(self,lat,long,dataHora, distanciaPercorrida):
        self.__lat = lat
        self.__lng = long
        self.__dataHora = dataHora
        self.__distanciaPercorrida = distanciaPercorrida
        
    @property
    def lat(self):
        return self.__lat
    
    @property
    def lng(self):
        return self.__lng
    
    @property
    def dataHora(self):
        return self.__dataHora
        
    @property
    def distanciaPercorrida(self):
        return self.__distanciaPercorrida