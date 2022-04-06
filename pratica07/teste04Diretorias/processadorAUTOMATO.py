import sys
import ply.lex as lex


#Lista de tokens, tem de ser caseSensitive para as funcoes serem mapeadas corretamente
tokens =["id"]

literals = "{ } ,".split(" ")

def t_id(t):
    r'[\w.\-]+'
    print(t.value,end=' ')
    return t

def t_eof(t):
    print("\nPrograma Terminou!")

# Isto nunca vai acontecer
def t_error(t):
    r'.'
    print("Erro!")
    t.lexer.skip(1)

#Build the lexer
processador = lex.lex()


str_teste = 'PL{DOC{TP},AULAS{03-13{DB{},x.py}}}'

#Give the lexer some input
processador.input(str_teste)

#Tokenize
processador.token()

print("Tokenize Terminou \n");
