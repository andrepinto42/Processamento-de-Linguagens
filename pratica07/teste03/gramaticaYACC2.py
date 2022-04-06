#!usr/bin//env python3 
# Yacc example 
import ply.yacc as yacc
from gramaticaPLY2 import tokens 
import sys

literals = "[ ] ,".split(" ") # [ "[" , "]" , ","]

def p_Li1(p):
    r"Li : '[' ni ':' ni ']'"
    p[0] =list( range(p[2],p[4]+1))

def p_Li2(p):
    r"Li : '[' Es ']'"
    p[0] = p[2]

def p_Li3(p):
    r"Li : '[' ']'"
    p[0] = []

def p_Es1(p):
    "Es : N ',' Es"
    p[0] = [p[1]] + p[3]

def p_Es2(p):
    "Es : N"
    p[0] = [p[1]]

def p_N1(p):
    r"N : Li"
    p[0] = p[1]

def p_N2(p):
    r"N : ni"
    p[0] = p[1]

def p_error(p):
    print("Error in",p)

# Build the parser
parser = yacc.yacc()
 
str = "[7,[],[12,[8]],9,[20:26]]"

if(len(sys.argv) == 1):
    str = sys.stdin.read()
else:
    str = open(sys.argv[1]).read()


result = parser.parse(str)
print("Resultado =",result)
# Para debugging
#while tok:= lexer.token() : print(tok)
