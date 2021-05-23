import ply.yacc as yacc
import sys

#Get the token from 
from trabalho_lex import tokens, literals, lexer

#Producion rules
def p_Code(p):
    "CODE : DECLS INSIDE"
    print("START")
    print(p[1], end='')
    #print(p[2], end='')
    print("STOP")

def p_DECLS_DECLS1(p):
    "DECLS : DECLS DECL ';'"
    p[0] = p[1] + p[2]

def p_DECLS_DECL(p):
    "DECLS : DECL ';'"
    parser.lines += 1
    p[0] = p[1]

#def p_DECLS_DECLS2(p):
#    "DECLS : DECLS DECLA ';'"
#    p[0] = p[1] + p[2]

#def p_DECLS_DECLA(p):
#    "DECLS : DECLA ';'"
#    p[0] = p[1]

def p_INSIDE_INSIDE(p):
    "INSIDE : INSIDE INFO"
    p[0] = p[1] + p[2]

def p_INSIDE_INFO(p):
    "INSIDE : INFO"
    p[0] = p[1]

#def p_INFO_ATUL(p):
#    "INFO : ATUL ';'"
#    p[0] = p[1]

#def p_INFO_MATH(p):
#    "INFO : MATH ';'"
#    p[0] = p[1]

#def p_INFO_IFBLOCK(p):
#    "INFO : IFBLOCK"
#    p[0] = p[1]

#def p_INFO_REPEATBLOCK(p):
#    "INFO : REPEATBLOCK"
#    p[0] = p[1]

def p_INFO_PRINT(p):
    "INFO : PRINT '(' VALOR ')' ';'"
    parser.lines += 1
    p[0] = p[1] + "WRITEI\n"

#def p_INFO_RETURN(p):
#    "INFO : RETURN VALOR ';'"
#    p[0] = p[1]


def p_DECL_ID(p):
    "DECL : INT ID"
    if (p[2] in p.parser.variables.keys()):
        print("Erro na linha ", parser.lines)
        print("A variavel ", p[2], " já existe")
    else:
        p.parser.variables.update({p[2]: parser.offset_var})
        parser.offset_var += 1
        p[0] = "PUSHI 0\n"

def p_DECL_VALOR(p):
    "DECL : INT ID '=' VALOR"
    if (p[2] in p.parser.variables.keys()):
        print("Erro na linha ", parser.lines)
        print("A variavel ", p[2], " já existe")
    else:
        p.parser.variables.update({p[2]: parser.offset_var})
        parser.offset_var += 1
        p[0] = "PUSHI 0\n" + p[4] + "STOREG " + str(parser.offset_var-1) + "\n"

def p_VALOR_VALOR1(p):
    "VALOR : VALOR1"
    p[0] = p[1]

def p_FACTOR_READ(p):
    "VALOR : READ '(' ')'"
    p[0] = "READ\nATOI\n"

def p_VALOR1_NUM(p):
    "VALOR1 : NUM"
    p[0] = "PUSHI " + p[1] + "\n"

def p_VALOR1_ID(p):
    "VALOR1 : ID"
    if(p[1] not in p.parser.variables.keys()):
        print("Erro na linha ", parser.lines)
        print("A variavel ", p[1], " não existe")
    else:
        res = p.parser.variables.get(p[1])
        p[0] = "PUSHG " + str(res) + "\n"

def p_VALOR1_MATH(p):
    "VALOR1 : MATH"
    p[0] = p[1]

def p_MATH_ADD(p):
    "MATH : MATH '+' TERMO"
    p[0] = p[1] + p[3] + "ADD" + "\n"

def p_MATH_SUB(p):
    "MATH : MATH '-' TERMO"
    p[0] = p[1] + p[3] + "SUB" + "\n"

def p_MATH_TERMO(p):
    "MATH : TERMO"
    p[0] = p[1]

def p_TERMO_MUL(p):
    "TERMO : TERMO '*' FACTOR"
    p[0] = p[1] + p[3] + "MUL" + "\n"

def p_TERMO_DIV(p):
    "TERMO : TERMO '/' FACTOR"
    p[0] = p[1] + p[3] + "DIV" + "\n"

def p_TERMO_FACTOR(p):
    "TERMO : FACTOR"
    p[0] = p[1]

def p_FACTOR_VALOR(p):
    "FACTOR : VALOR"
    p[0] = p[1]

#def p_FACTOR_MATH(p):
#    "FACTOR : MATH"
#    p[0] = p[1]

#def p_FACTOR_MATH1(p):
#    "FACTOR : '(' MATH ')'"
#    p[0] = p[1]

def p_error(p):
    print(parser.lines)
    print("Syntax error in input!")

#Build the parser
parser = yacc.yacc()

#My state
parser.variables = {}
parser.arrays = {}
parser.offset_var = 0
parser.offset_arr = 0
parser.lines = 1

#Read line input and parse it

f = open("trial.c", "r").read()

parser.parse(f)