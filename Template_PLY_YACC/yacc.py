import ply.yacc as yacc
from test import tokens 
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
    "comando : Exp"
    print(p[1])

def p_atrib(p):
    "atrib : ID '=' Exp"
    #Criar a variavel caso ela nao exista e atualizar
    p.parser.tabela_ids[p[1]] = p[3]

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
    print("Error in",p)

parser = yacc.yacc()

#Gerar uma tabela para guardar todos os ID
parser.tabela_ids = {}


str_testInput = '''
a = 4+5
a
5+5
'''


parser.parse(str_testInput)
quit()

# for line in sys.stdin:
#     parser.parse(line)
