import ply.yacc as yacc
from calc import tokens 
import sys

def p_prog(p):
    "prog : comandos"

def p_comandos_varios01(p):
    "comandos : "

def p_comandos_varios02(p):
    "comandos : comandos comando"

def p_comando01(p):
    "comando : atrib"
    

def p_comando02(p):
    "comando : print"
    
def p_comando03(p):
    "comando : read"
    
def p_comando04(p):
    "comando : dump"
    

def p_atrib(p):
    "atrib : ID '=' Exp"
    #Criar a variavel caso ela nao exista e atualizar
    p.parser.tabela_ids[p[1]] = p[3]

def p_print(p):
    "print : PRINT Exp"
    print(p[2])

def p_read(p):
    "read : READ ID"
    r = int(input())
    p.parser.tabela_ids[p[2]] = r
    
def p_dump(p):
    "dump : DUMP"
    print(p.parser.tabela_ids)

def p_Exp01(p):
    "Exp : Exp '+' Exp"
    p[0] = p[1] + p[3]

def p_Exp02(p):
    "Exp : Exp '-' Exp"
    p[0] = p[1] - p[3]

def p_Exp03(p):
    "Exp : INT"
    p[0] = p[1]

def p_Exp04(p):
    "Exp : ID"
    if p[1] in p.parser.tabela_ids:
        p[0] = p.parser.tabela_ids[p[1]]
    else:
        print("Variavel nao definida!, vai ser assumida como 0")
        p[0] = 0

def p_error(p):
    print("Error")

parser = yacc.yacc()
parser.tabela_ids = {}



for line in sys.stdin:
    parser.parse(line)
