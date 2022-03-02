import re
import sys

#\b verifica por qualquer carater que nao é alpha numerico

#Caca uma palavra em um texto
# e depois procura a palavra que encontrou antes atraves do \1
palavraDobrada = r'\b(\w+)\s+\1\b'

pint = re.compile(palavraDobrada)

for linha in sys.stdin:
    m = pint.search(linha)
    if (not m):
        print("No match bro")
        continue;
    
    print("Group  = " + str(m.group()))