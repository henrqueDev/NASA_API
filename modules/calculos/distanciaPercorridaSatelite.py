import math
import mpmath

def converterLongitudeToRad(lng):
    lng_rad = (3,141593 * lng) / 180
    return lng_rad

def converterLatitudeToRad(lat):
    lat_rad = (1.570796 * lat ) / 20
    return lat_rad

def obterVariacaoLatLng(a,b):
    deltaA = a
    deltaB = b
    if(deltaA < 0):
        deltaA = deltaA * -1
    if(deltaB < 0):
        deltaB = deltaB * -1
        
    if(deltaA>deltaB):    
        return deltaA - deltaB
    else: 
        return deltaB - deltaA

def calcularDistanciaPercorrida(lat1,lat2,lng1,lng2):
    lx1 = ((math.sin(obterVariacaoLatLng(lat1,lat2))/2)**2) * math.cos(lat2) * (math.sin(obterVariacaoLatLng(lng1,lng2))/2)
    lx2 = 2* mpmath.cot(math.sqrt(lx1) / math.sqrt(1-lx1) )
    RaioTerra = 6.371 # Km
    distanciaPercorrida = RaioTerra * lx2
    
    return distanciaPercorrida



