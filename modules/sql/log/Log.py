class Log:
    def __init__(self,lat,long,dataHora, distanciaPercorrida):
        self.__lat = lat
        self.__long = long
        self.__dataHora = dataHora
        self.__distanciaPercorrida = distanciaPercorrida
        
    @property
    def lat(self):
        return self.__lat
    
    @property
    def long(self):
        return self.__long
    
    @property
    def dataHora(self):
        return self.__dataHora
        
    @property
    def distanciaPercorrida(self):
        return self.__distanciaPercorrida