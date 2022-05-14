import sys
import ply.lex as lex

# Vao existir 2 estados
# O estado INITIAL é o predefinido pelo lexer
states = [
    ('INATIVO','inclusive') #Estado definido
]

#Lista de tokens, tem de ser caseSensitive para as funcoes serem mapeadas corretamente
tokens ="ON OFF NUMERO PRINT".split(" ")

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.lexer.soma += float( t.value)
    
    print(t.value,end='')

def t_INATIVO_NUMERO(t):
    r'\d+(\.\d+)?'
    print(t.value,end='')


#?i serve para tornar o resto case insensitive
def t_ON(t):
    r'\b(?i:on)\b'
    t.lexer.begin('INITIAL')

def t_OFF(t):
    r'\b(?i:off)\b'
    t.lexer.begin('INATIVO')

def t_PRINT(t):
    r'='
    print(t.lexer.soma,end='')

def t_eof(t):
    print("\nPrograma Terminou!")

#Serve para imprimir o texto de input do programa
# Todos os carateres que nao fazem parte da gramatica são imprimidos 
def t_default(t):
    r'(.|\n)'
    print(t.value,end='')
    pass

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
