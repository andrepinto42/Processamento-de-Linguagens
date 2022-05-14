import ply.lex as lex

reservadas = "int str print while".split()

tokens =("ID NUM STRING" + reservadas.upper()).split(" ")

literals = "= + - * / ( ) ^ \n . ;".split()

#LEXER
def t_INT(t):
    r'\d+'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'".*?"'
    return t

#ID tem de aparecer depois das palavras reservadas se nao vai conseguir PRINT como um id
def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

def t_PRINT(t):
    r'(?i)PRINT'
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
]

def p_prog(p):
    "prog : decls instrs"
    print(f'{p[1]} start\n {p[2]}stop\n')

def p_decls02(p):"decls : ";p[0] = ""
def p_decls01(p):
    "decls : decls decl"
    p[0] = p[1] + p[2]


def p_decl01(p): 
    "decl : INT ID ';'"
    p.parser.symbols[p[2]] = (p.parser.symbols["sp"],'num')
    p.parser.symbols["sp"] += 1
    
    #Talvez esteja errado
    p[0] = ('num','pushi 0\n')

def p_instrs01(p):"instrs : "; p[0] = ""
def p_instrs02(p):"instrs : instrs instr "; p[0] = p[1] + p[2]

def p_instr01(p):
    "instr : ID '=' exp ';'"
    if p[1] in p.parser.symbols:
        end, tipo = p.parser.symbols[p[1]]
        tipoExp,valExp= p[3]
        if tipo != tipoExp:
            error("Erro de tipos")

        p[0] = f'{valExp}storeg {end}\n' 
    else:
        print(f'Variable {p[1]} has not been declared!')
        quit()

def p_instr02(p):
    "instr : PRINT exp ';'" 
    tipo,val = p[2]
    if tipo is 'num':
        p[0] = f'{val}writei\n'
    else
        p[0] = f'{val}writes\n'

def p_instr03(p):
    "instr : WHILE '(' exp ')' instr" 
    mylabel = p.parser.labels

    p[0] = f'while{mylabel}:\n{p[3][1]}jz fim{mylabel}\n{p[5]}\njump while{mylabel}\nfim{mylabel}'

def p_instr04(p):
    "ins"

def p_exp_add(p):       
    "exp : exp '+' exp"            
    type1,val1 = p[1]
    type2,val2 = p[3]

    if type1 is 'num' and type2 is 'num':
        p[0] = f'{p[1]}{p[3]}add\n'
    else:
        p[0] = ('str',f'{val1}{val2}concat\n')

def p_exp_sub(p):       "exp : exp '-' exp";            p[0] = f'{p[1][1]}{p[3][1]}sub\n'
def p_exp_mult(p):      "exp : exp '*' exp";            p[0] = f'{p[1][1]}{p[3][1]}mul\n'
def p_exp_dividir(p):   "exp : exp '/' exp";            p[0] = f'{p[1][1]}{p[3][1]}div\n'
def p_exp_chapeu(p):    "exp : exp '^' exp";  

def p_exp_Int(p):       
    "exp : INT"
    p[0] = f'pushi {p[1]}\n'

def p_exp_NUM(p):
    "exp : NUM"
    p[0] = f'pushi {p[1]}\n'

#Devolve um zero se o atributo nao existir na tabela
def p_exp_ID(p):        
    "exp : ID"          
    if p[1] in p.parser.symbols:
        end,tipo = p.parser.symbols[p[1]]
        p[0] = f'pushg {end}\n'
    else:
        error(f'Variable {p[1]} has not been declared!\n')


def p_exp_parenteses(p):"exp : '(' exp ')'"; 
def p_exp_ponto(p):     "exp : '.'";         

def p_exp_String(p):
    "exp : STRING"
    p[0] = ('str',f'pushs {p[1]}\n')

def p_error(p):
    print("Error")

#Build the yacc parser
parser = yacc.yacc()

#Initialize the variable dictionary
parser.tabela_ids = {}

#Erro aqui nao é assim representada a estrutura de dados
parser.symbols = { "sp":0 }

print("Parser initialized, start typing\n$ ",end='')
for line in sys.stdin:
    parser.parse(line)
    print("\n$ ",end='')