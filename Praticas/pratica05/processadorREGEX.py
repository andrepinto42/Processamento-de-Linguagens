import sys
import ply.lex as lex
import re


#Lista de tokens, tem de ser caseSensitive para as funcoes serem mapeadas corretamente
tokens ="ON OFF NUMERO PRINT".split(" ")

contador = 0
ativo = True

for linha in sys.stdin:
    if m:=re.search(r'(?P<NUM>\d+(\.\d+)?)',linha):
        if ativo:
            contador += float(m.group())

    elif m:=re.search(r'(?P<ON>\b(?i:on)\b)',linha):
        ativo = True

    elif m:=re.search(r'(?P<OFF>\b(?i:off)\b)',linha):
        ativo = False
    
    elif m:=re.search(r'=',linha):
        print("Total =",contador)
    else:
        print(linha,end='')
    