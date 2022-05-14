from re import *
from ply.lex import lex

'''
DSVR -> SRs

SRs -> SRs SR
    | SR

SR -> RMDEF ID SUBS '.'
    t[0] = f'''
def {p[2]}(t):
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
            return texto'''

SUBS -> SUBS SUB
     | SUB

SUB -> TEXTO '->' TEXTO

SUB -> SUBT
: ls,rs = p[1]

: t[0] = f'\tt,n1 = subn(rf'{ls}',rf'{rs},t); n+=n1\n'
'''