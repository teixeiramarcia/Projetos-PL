import ply.yacc as yacc
import sys

#Get the token from 
from trabalho_lex import tokens, literals

#Producion rules
def p_Code(p):
    "CODE : DECLS INSIDE"
    #p_DECLS(p[1])
    #p_INSIDE(p[2])
    pass

def p_DECLS_DECL(p):
    "DECLS : DECLS DECL ';'"
    #p_DECLS(p[1])
    #p_DECL(p[2])
    pass

def p_DECLS_DECLA(p):
    "DECLS : DECLS DECLA ';'"
    #p_DECLS(p[1])
    #p_DECLA(p[2])
    pass

def p_DECLS_VAZIO(p):
    "DECLS : Vazio"
    pass

def p_DECL_ID(p):
    "DECL : INT ID"
    if (p[2] in p.parser.variables.keys()):
        print("Erro na linha ", lines)
        print("A variavel ", p[2], " já existe")
    else:
        p.parser.variables[p[2]] = [offset_var, 0]
        offset_var += 1
        print("PUSHI 0")

def p_DECL_VALOR(p):
    "DECL : INT ID '=' VALOR"
    if (p[2] in p.parser.variables.keys()):
        print("Erro na linha ", lines)
        print("A variavel ", p[2], " já existe")
    else:
        p.parser.variables[p[2]] = [offset_var, p[4]]
        offset_var += 1
        print("PUSHI ", p[4])

def p_DECLA_VAR(p):
    "DECLA : INT ID '[' VALOR1 ']'"
    if (p[2] in p.parser.arrays.keys()):
        print("Erro na linha ", lines)
        print("A variavel ", p[2], " já existe")
    elif (p[4] == 0):
        print("Erro na linha ", lines)
        print("O valor do tamanho do array não pode ser 0")
    elif (p[4] < 0):
        print("Erro na linha ", lines)
        print("O valor do tamanho do array ", p[4], " não pode ser negativo")
    else:
        lista = []
        for i in range(0,p[4]):
            lista.append(0)
        p.parser.arrays[p[2]] = [offset_var, offset_var+p[4]-1,lista]
        offset_var += p[4]
        print("PUSHN ", p[4])

def p_ATUL_ID(p):
    "ATUL : ID '=' VALOR"
    if (p[1] not in p.parser.variables.keys()):
        print("Erro na linha ", lines)
        print("A variavel ", p[1], " não existe")
    else:
        variavel = p.parser.variables.get(p[1])
        variavel[1] = p[3]
        print("PUSHI ", p[4])
        print("STOREG ", variavel[0])

def p_ATUL_ARRAY(p):
    "ATUL : ID '[' VALOR1 ']' '=' VALOR"
    if (p[1] not in p.parser.arrays.keys()):
        print("Erro na linha ", lines)
        print("A variavel ", p[1], " não existe")
    elif (p[3] < 0 || p[3] > p.parser.arrays.get(p[1])[1] - p.parser.arrays.get(p[1])[0]):
        print("Erro na linha ", lines)
        print("O valor do tamanho do array ", p[3], " está fora do tamanho do array")
    else:
        variavel = p.parser.arrays.get(p[1])
        variavel[2][p[3]] = p[6]
        print("PUSHI ", p[4])
        print("STOREG ", variavel[0]+p[3]) 

def p_VALOR_VALOR1(p):
    "VALOR : VALOR1"
    p[0] = p[1]

def p_VALOR_READ(p): #Duvida read
    "VALOR : READ"
    print("READ")
    print("ATOI")
    p[0] = p[1]

def p_VALOR1_NUM(p):
    "VALOR1 : NUM"
    p[0] = p[1]

def p_VALOR1_ID(p):
    "VALOR1 : ID"
    if(p[1] not in p.parser.variables.keys()):
        print("Erro na linha ", lines)
        print("A variavel ", p[1], " não existe")
    else:
        p[0] = p.parser.variables.get(p[1])[1]

def p_VALOR1_MATH(p):
    "VALOR1 : MATH"
    p[0] = p[1]

def p_VALOR1_ARRAY(p):
    "VALOR1 : ID '[' VALOR1 ']'"
    if(p[1] not in p.parser.arrays.keys()):
        print("Erro na linha ", lines)
        print("A variavel ", p[1], " não existe")
    else:
        p[0] = p.parser.variables.get(p[1])[2][p[3]]

def p_MATH_ADD(p):
    "MATH : MATH '+' TERMO"
    print("ADD")

def p_MATH_SUB(p):
    "MATH : MATH '-' TERMO"
    print("SUB")

def p_MATH_TERMO(p):
    "MATH : TERMO"
    p[0] = p[1]

def p_TERMO_MUL(p):
    "TERMO : TERMO '*' FACTOR"
    print("MUL")

def p_TERMO_DIV(p):
    "TERMO : TERMO '/' FACTOR"
    if(p[1]!=0):
        print("DIV")
    else:
        print("Erro: divisão por 0, a continunar com 0")
        p[0] = 0

def p_TERMO_FACTOR(p):
    "TERMO : FACTOR"
    p[0] = p[1]

def p_FACTOR_MATH(p):
    "FACTOR : MATH"
    p[0] = p[1]

def p_FACTOR_GROUP(p):
    "FACTOR : '(' MATH ')'"
    p[0] = p[2]

def p_FACTOR_VALOR(p):
    "Factor : VALOR"
    p[0] = int(p[1])


#Build the parser
parser = yacc.yacc()

#My state
parser.variables = {}
parser.arrays = {}
offset_var = 0
offset_arr = 0
lines = 1

#Read line input and parse it
import sys
for linha in sys.stdin:
    result = parser.parse(linha)
    lines += 1
    print(result)
