# Yacc example 
import ply.yacc as yacc
from gramaticaPLY2 import tokens
 

literals = "[ ] ,".split(" ") # [ "[" , "]" , ","]

def p_Li1(p):
    r"Li : '[' E ']'"
    p[0] = p[2]


def p_Li2(p):
    r"Li : '[' ']'"
    p[0] = 0

def p_E1(p):
    r"E : N ',' E"
    p[0] = p[1] + p[3]

def p_E2(p):
    r"E : N"
    p[0] = p[1]

def p_N1(p):
    r"N : Li"
    p[0] = p[1]

def p_N2(p):
    r"N : ni"
    p[0] = 1

def p_error(p):
    print("Error!")

 
 # Build the parser
parser = yacc.yacc()
 
str = "[7,[],[12,[8]],9]"

# Para debugging
#while tok:= lexer.token() : print(tok)


result = parser.parse(str)
print("Numero de inteiros",result)