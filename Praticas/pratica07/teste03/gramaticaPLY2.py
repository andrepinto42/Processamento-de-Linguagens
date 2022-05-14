import ply.lex as lex
 

#Lista de tokens, tem de ser caseSensitive para as funcoes serem mapeadas corretamente
tokens ="ni".split(" ")

literals = "[ ] ,".split(" ")

def t_ni(t):
    r'\d+'
    t.value = int( t.value)
    print(t.value,end=' ')
    return t

def t_eof(t):
    print("\nPrograma Terminou!")

# Isto nunca vai acontecer
def t_error(t):
    r'.'
    t.lexer.skip(1)
 
 # Build the parser
lexer = lex.lex()
 
str = "[7,[],[12,[8]],9]"

lexer.input(str)

# Para debugging
#while tok:= lexer.token() : print(tok)


#Tokenize
lexer.token()