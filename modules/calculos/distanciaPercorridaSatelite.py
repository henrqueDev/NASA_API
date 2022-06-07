import math
import mpmath

def converterLatLongToRad(latLong):
    latLong_rad = latLong * (3.141593 / 180)
    return latLong_rad

def obterVariacaoLatLng(a,b):
    deltaA = a
    deltaB = b
    variacao = (deltaA - deltaB)
    if(variacao < 0):
        #print('deltaA to positive')
        variacao = (deltaA - deltaB) * -1
    
    print(variacao)
    return variacao
def calcularDistanciaPercorrida(lat1,lat2,lng1,lng2):
    lx1 = (((math.sin(obterVariacaoLatLng(lat1,lat2))/2)**2) + math.cos(lat1)) * math.cos(lat2) * ((math.sin(obterVariacaoLatLng(lng1,lng2)/2)) ** 2)
    try :
        print(lx1)
        lx3 = mpmath.cot(math.sqrt(0.41666) / math.sqrt(1-0.41666) )
        print(lx3)
        lx2 = 2 * lx3
    except ZeroDivisionError:
        lx2 = 0
    print(lx2)
    RaioTerra = 6.371 # Km
    distanciaPercorrida = RaioTerra * lx2
    
    return distanciaPercorrida



a = converterLatLongToRad(34)
b = converterLatLongToRad(35)
c = converterLatLongToRad(118)
d = converterLatLongToRad(139)

n = calcularDistanciaPercorrida(0.5942 ,0.6227,-2.0634,2.4387)
print(n)

"""

SUBSTITUIR COT POR ARCO TANGENTE

"""