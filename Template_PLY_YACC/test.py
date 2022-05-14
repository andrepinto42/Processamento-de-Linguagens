import ply.lex as lex

tokens =["ID","INT"]

literals = ['=','+','-']



def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

#ID tem de aparecer depois das palavras reservadas se nao vai conseguir PRINT como um id
def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

t_ignore = ' \n\t\r'

def t_error(t):
    print("Wrong character!", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

# import sys

# for line in sys.stdin:
#     lexer.input(line)
#     for tok in lexer:
#         print(tok)