import sys
import re


def tokenize(code):
    token_specifications = [
        ('NUM', r'\d+'),
        ('ATRIB', r'='),
        ('ID', r'[_A-Za-z]\w*'),
        ('OP', r'[+\-*/]'),
        ('NEWLINE', r'\n'),
        ('SKIP', r'[ \t]+'),
        ('ERROR', r'.'),
    ]

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specifications)
    reconhecidos = []
    match_objects = re.finditer(tok_regex, code)
    #Valor para ser incrementado
    linha = 1
    for m in match_objects:
        dictionary = m.groupdict()
        
        if dictionary['NUM'] is not None:
            t = ("NUM",int(dictionary['NUM']),linha,m.span() )
        elif dictionary['ATRIB'] is not None:
            t = ("ATRIB","=",linha,m.span() )
        elif dictionary['ID'] is not None:
            t = ("ID",dictionary['ID'],linha,m.span() )
        #Repetir estes passos
        else:
            t = ("ERRO",m.group(),linha,m.span() )
        
        reconhecidos.append(t)
    
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)