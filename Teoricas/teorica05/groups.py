import re
import sys

# Ao colocar os parentes entre o \d+ criamos um novo grupo
inteiro = r'(\+|-)?(\d+)'

#real = r'(\+|-)?(\d+)(\.\d+)?'
#?: significa que o grupo nao vai ser capturado
real = r'(\+|-)?(\d+)(?:\.(\d+))?'

pint = re.compile(inteiro)
preal = re.compile(real)

for linha in sys.stdin:
    m = pint.search(linha)
    n = preal.search(linha)
    print("Groups = " +str(n.groups()))
    print("Group  = " + str(n.group()))