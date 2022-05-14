import ply.lex as lex

codigo = '''
func(int a){
    char batata;
    if (a){
        a= 123;
    }
}
'''

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
)


#Lista de tokens, tipos de coisas que vao ser retornadas
tokens ="ID INT CHAR IF INTEIRO".split(" ")

#
literals = "* + - / = ( ) { }".split(" ")

#
reservadas = "if else int char bool".split(" ")

def t_Inteiro(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    # Se a palavra for if entao transform o tipo em IF
    if t.value in reservadas:
        t.type = t.value.upper()
    return t

t_ignore =' \t\n'

def t_error(t):
    print("Ilegall Character",t)
    t.lexer.skip(1)

#Build the lexer
processador = lex.lex()


#Give the lexer some input
processador.input(codigo)


#Tokenize
while tok:=processador.token():
    print(tok)
