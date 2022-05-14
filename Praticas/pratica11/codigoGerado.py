from re import *

def FIX(texto):
    texto = sub('marco','Marco',texto)
    texto = sub('200\s+escudos','1€',texto)
    return texto


def FIX2(texto):
    texto = sub('@',' at ',texto)
    texto = sub('[.]',' ponto ',texto)
    return texto

def EN2PT(texto):
    texto = "_" + texto
    while(True):
        texto,num1 = subn('_the','o_',texto)
        texto,num2 = subn('_cat','gato_',texto)
        texto,num3 = subn('_is sleeping','esta a dormir_',texto)
        
        #Caso nenhuma substituição tenha acontecido
        if (num1 + num2 + num3 == 0):    
            texto,num4 = subn('_(.)',r'\1_',texto)

        #Caso a nossa marca se encontre no final do texto
        if search(r'_$',texto):
                return texto

