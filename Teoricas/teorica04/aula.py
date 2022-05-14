import re

### First part
p = re.compile(r'\d+')
print(p.match("ola"))

print( p.match("12").group() )
print( p.match("12").start() )
print( p.match("12").end() )
print( p.match("12").span() )


### Second Part

def recon(texto):
    m = re.match(r'Hoje',texto)
    if m:
        print("Encontrado: ",m.group())
    else:
        print("Nao encontrado")
        
recon("123")   


### Third Part

def reconAll(texto):
    m = re.findall(r'\d+',texto)
    if m:
        print("Encontrado: ",m)
    else:
        print("Nao encontrado")

 
reconAll("123 + 456 = 999")


### 4th Part

def reconIter(texto):
    m = re.finditer(r'\d+',texto)
    if m:
        for obj in m:   
            print("Encontrado: ",obj.group())
    else:
        print("Nao encontrado")

reconIter("123 + 456 = 999")

### 5th Part

import sys

for linha in sys.stdin:
    print(linha)