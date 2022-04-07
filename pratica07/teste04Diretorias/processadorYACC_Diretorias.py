#!usr/bin//env python3 
# Yacc example 
import ply.yacc as yacc
from processadorAUTOMATO import tokens 
import sys

literals = "{ } ,".split(" ") # [ "[" , "]" , ","]

def p_FS(p):
    "FS : Dir"
    p[0] = p[1]

def p_Dir1(p):
    "Dir : id '{' Filhos '}'"
    p[0] = f'mkdir {p[1]} && cd {p[1]} \n{p[3]}cd ..\n'
    

def p_Dir2(p):
    "Dir : id '{' '}'"
    p[0] = f'mkdir {p[1]}\n'

def p_Filhos1(p):
    "Filhos : Filho"
    p[0] = p[1]

def p_Filhos2(p):
    "Filhos : Filho ',' Filhos"
    # Forcar o yacc a guardar os Filhos como resultado?
    p[0] = p[1] + p[3];

def p_Filho1(p):
    "Filho : id"
    p[0] = f'touch {p[1]}\n'

def p_Filho2(p):
    "Filho : Dir"
    p[0] = p[1]

def p_error(p):
    print("Error in",p)

# Build the parser
parser = yacc.yacc()
 

str = 'PL{DOC{TP},AULAS{03-13{DB{},x.py}}}'


if len(sys.argv) == 2:
    str = open(sys.argv[1]).read()

print("\nString Inicial",str);
result = parser.parse(str)
print("Resultado ->\n\n",result)


import os

# usar o sh para utilizar um ficheiro como se fosse comandos da bash
os.system(result)

# Para debugging
#while tok:= lexer.token() : print(tok)
