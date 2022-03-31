import sys
import ply.lex as lex

# Vao existir 2 estados
# O estado INITIAL é o predefinido pelo lexer
states = [
    ('INATIVO','inclusive') #
]

#Lista de tokens, tem de ser caseSensitive para as funcoes serem mapeadas corretamente
tokens ="ni".split(" ")

literals = "[ ] ,".split(" ")

def t_ni(t):
    r'\d+'
    t.value = int( t.value)
    print(t.value,end='')
    return t

def t_eof(t):
    print("\nPrograma Terminou!")

# Isto nunca vai acontecer
def t_error(t):
    r'.'
    t.lexer.skip(1)

#Build the lexer
processador = lex.lex()

codigo = open( sys.argv[1]).read()

#Give the lexer some input
processador.input(codigo)

#Inicializar a variavel que conta o preco de todos os produtos do lexer a 0
processador.soma = 0

#Tokenize
processador.token()


#Codigo desnecessario ?
while True:
    tok = processador.token()
    if not tok:
        break
    print(tok)