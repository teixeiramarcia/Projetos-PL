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

def p_DECLA_NUM(p):
    "DECLA : INT ID '[' NUM ']'"
    if (p[2] in p.parser.arrays.keys()):
        print("Erro na linha ", lines)
        print("A variavel ", p[2], " já existe")
    elif (p[4] < 0 || p[4] > p.parser.arrays.get(p[2])[1] - p.parser.arrays.get(p[2])[0]):
        print("Erro na linha ", lines)
        print("O valor do tamanho do array ", p[4], " está fora do tamanho do array")
    elif (p[4] == 0):
        print("Erro na linha ", lines)
        print("O valor do tamanho do array não pode ser 0")
    else:
        lista = []
        for(i=0;i<p[4];i++):
            lista.append(0)
        p.parser.arrays[p[2]] = [offset_var, offset_var+p[4]-1,lista]
        offset_var += p[4]
        print("PUSHN ", p[4])

def p_DECLA_ID(p):
    "DECLA : INT ID '[' ID ']'"
    if (p[2] in p.parser.arrays.keys()):
        print("Erro na linha ", lines)
        print("A variavel ", p[2], " já existe")
    elif (p[4] not in p.parser.variables.keys()):
        print("Erro na linha ", lines)
        print("A variavel", p[4], " não existe")
    elif (p[4] < 0 || p[4] > p.parser.arrays.get(p[2])[1] - p.parser.arrays.get(p[2])[0]):
        print("Erro na linha ", lines)
        print("O valor do tamanho do array ", p[4], " está fora do tamanho do array")
    elif (p[4] == 0):
        print("Erro na linha ", lines)
        print("O valor do tamanho do array não pode ser 0")
    else:
        tamanho_array = p.registers.variables.get(p[4])[1]
        lista = []
        for(i=0;i<tamanho_array;i++):
            lista.append(0)
        p.parser.arrays[p[2]] = [offset_var, offset_var+tamanho_array-1, lista]
        offset_var += tamanho_array
        print("PUSHN ", p[3])

def p_DECLA_NUM(p):
    "DECLA : INT ID '[' MATH ']'"
    if (p[2] in p.parser.arrays.keys()):
        print("Erro na linha ", lines)
        print("A variavel ", p[2], " já existe")
    elif (p[4] < 0 || p[4] > p.parser.arrays.get(p[2])[1] - p.parser.arrays.get(p[2])[0]):
        print("Erro na linha ", lines)
        print("O valor do tamanho do array ", p[4], " está fora do tamanho do array")
    elif (p[4] == 0):
        print("Erro na linha ", lines)
        print("O valor do tamanho do array não pode ser 0")
    else:
        lista = []
        for(i=0;i<p[4];i++):
            lista.append(0)
        p.parser.arrays[p[2]] = [offset_var, offset_var+p[4]-1,lista]
        offset_var += p[4]
        print("PUSHN ", p[4])

def p_Comando_dump(p):
    "Comando : DUMP"
    print(p.parser.registers) 

def p_Exp_add(p):
    "Exp : '(' ADD Exp Termo ')'"
    p[0] = p[3] + p[4]

def p_Exp_sub(p):
    "Exp : '(' SUB Exp Termo ')'"
    p[0] = p[3] - p[4]

def p_Exp_termo(p):
    "Exp : Termo"
    p[0] = p[1]

def p_Termo_mul(p):
    "Termo : '(' MUL Termo Factor ')'"
    p[0] = p[3] * p[4]

def p_Termo_div(p):
    "Termo : '(' DIV Termo Factor ')'"
    if(p[4!=0]):
        p[0] = p[3] / P[4]
    else:
        print("Erro: divisão por 0. A continuar com o dividendo: ", p[3])
        p[0] = p[3]
    
def p_Termo_factor(p):
    "Termo : Factor"
    p[0] = p[1]

def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]

def p_Factor_num(p):
    "Factor : NUM"
    p[0] = int(p[1])

def p_Factor_id(p):
    "Factor : ID"
    p[0] = p.parser.registers.get(p[1])

def p_error(p):
    print("Syntax error in input: ", p)

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
