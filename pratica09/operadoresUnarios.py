import ply.lex as lex

tokens =["ID","INT","PRINT","DUMP","NEGATE"]
literals = "= + - * / ( ) ^ \n . % , :".split()

#LEXER
def t_INT(t):
    r'\d+'
    t.value = float(t.value)
    return t

def t_PRINT(t):
    r'(print|PRINT)'
    return t

def t_DUMP(t):
    r'(dump|DUMP)'
    return t

#ID tem de aparecer depois das palavras reservadas se nao vai conseguir PRINT como um id
def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

def t_NEGATE(t):
    r'--'
    return t

t_ignore = ' \n\t\r'

def t_error(t):
    print("Wrong character!", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


# YACC
import ply.yacc as yacc
import sys
import math

precedence = [
    #Encontra-se no inicio entao tem a menor prioridade
    # a=b=c=0;
    ('right','='),
    ('left','+','-'),# Dont swap this line 
    ('left','*','/'),# for this line, it will reverse priority 
    ('right','^'),
    #encontra-se no fim da lista entao tem a maior prioridade
    ('right','NEGATE')
]

def p_prog(p):"prog : comandos"
def p_comandos_varios01(p):"comandos : "
def p_comandos_varios02(p):"comandos : comandos comando "

def p_comando01(p):"comando : ID '=' exp"; p.parser.tabela_ids[p[1]] = p[3]    

def p_comando02(p):"comando : exp"; print(p[1]); p.parser.tabela_ids['.'] = p[1]
def p_comando04(p):"comando : DUMP"; print(p.parser.tabela_ids)
def p_comando05(p):"comando : args";  print(p[1])
# def p_comando05(p):"comando : args"; p[0] = p[1]
    
def p_exp_add(p):       "exp : exp '+' exp"; p[0] = p[1] + p[3]
def p_exp_sub(p):       "exp : exp '-' exp"; p[0] = p[1] - p[3]
def p_exp_mult(p):      "exp : exp '*' exp"; p[0] = p[1] * p[3]
def p_exp_dividir(p):   "exp : exp '/' exp"; p[0] = p[1] / p[3]
def p_exp_chapeu(p):    "exp : exp '^' exp"; p[0] = p[1] **p[3]
def p_exp_Int(p):       "exp : INT";         p[0] = p[1]
#Devolve um zero se o atributo nao existir na tabela
def p_exp_ID(p):        "exp : ID";          p[0] = p.parser.tabela_ids.get(p[1],0)
def p_exp_parenteses(p):"exp : '(' exp ')'"; p[0] = p[2]
def p_exp_ponto(p):     "exp : '.'";         p[0] = p.parser.tabela_ids.get('.',0)
def p_exp_Negate(p): "exp : NEGATE exp";     p[0] = - p[2] 

#Devolver o p[3] como resultado da expressao
def p_exp_comboio(p):"exp : ID '=' exp"; p.parser.tabela_ids[p[1]] = p[3]; p[0] = p[3]    

#$ sin(4)
def p_exp_ExpressaoMatematica(p):
    "exp : ID '(' exp ')'"
    # assert  p.parser.funs[p[1]]['n'] is p[3]
    p[0] = p.parser.funs[p[1]]['c'](p[3])

def p_exp_ExpressaoMatematica2(p):
    "exp : ID '(' exp ',' exp ')'"
    # assert  p.parser.funs[p[1]]['n'] is p[3]
    p[0] = p.parser.funs[p[1]]['c'](p[3],p[5])

def p_args2(p): 
    "args : exp"
    p[0] = [p[1]]

def p_args3(p): 
    "args : args ',' exp"
    p[0] = p[1] + [p[3]]


def p_args4(p): 
    "args : exp ':' exp"
    p[0] = list(range(int(p[1]), int(p[3]) +1))

def p_error(p):
    print("Error")

#Build the yacc parser
parser = yacc.yacc()

#Initialize the variable dictionary
parser.tabela_ids = {'.': 0, 'pi' : math.pi}

parser.funs = {
    'sin': { 'c' : math.sin, 'n' : 1},
    'log': { 'c' : math.log, 'n' : 1},
    'pow': { 'c' : math.pow, 'n' : 2},
    #Definir uma funcao nossa para ser usada pelo parser ->
    #$ pinto1(3)
    #36
    'pinto1': { 'c' : lambda x : x +33, 'n' :1},
    #De momento nao funciona sum(5,6)
    'sum' : { 'c' : lambda *x : sum(x), 'n' : '*'}
}

print("Parser initialized, start typing\n$ ",end='')
for line in sys.stdin:
    parser.parse(line)
    print("\n$ ",end='')