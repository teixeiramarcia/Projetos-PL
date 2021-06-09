import ply.yacc as yacc
import re
import sys

#Get the token from 
from trabalho_lex import tokens, literals, lexer

#Producion rules
def p_TRIAL(p):
    "TRIAL : DECLS FUNCS"
    file = open("../vms-vf/vms/trial.vm", "w")
    file.write("START\n")
    file.write(p[1])
    file.write(p[2])
    file.write("FIMCODIGO:\n")
    file.write("STOP\n")
    file.close()

def p_FUNCS(p):
    "FUNCS : FUNCS FUNC"
    p[0] = p[2] + p[1]

def p_FUNCS_VAZIO(p):
    "FUNCS : FUNC"
    p[0] = p[1]

def p_FUNC(p):
    "FUNC : ID '{' CODE '}'"
    if (p[1] in parser.func or p[1] == "main"):
        print("Erro a funcão", p[1], " já existe")
    else:
        parser.func.append(p[1])
        parser.current_func = p[1]
        p[0] = p[1] + ":\n" + p[3]

def p_FUNC_MAIN(p):
    "FUNC : MAIN '{' CODE '}'"
    if (p[1] in parser.func):
        print("Erro a funcão", p[1], " já existe")
    else:
        parser.func.append(p[1])
        parser.current_func = p[1]
        p[0] = p[1] + ":\n" + p[3] + "JUMP FIMCODIGO\n"
        
def p_CODE(p):
    "CODE : INSIDE"
    p[0] = p[1]# + p[2]

def p_DECLS_DECL(p):
    "DECLS : DECLS DECL ';'"
    p[0] = p[1] + p[2]

#def p_DECLS_DECLA(p):
#    "DECLS : DECLS DECLA ';'"
#    p[0] = p[1] + p[2]

def p_DECLS_COMENTARIO(p):
    "DECLS : DECLS COMENTARIO"
    p[0] = p[1]

def p_DECLS_VAZIO(p):
    "DECLS : "
    p[0] = ""

def p_INSIDE_INSIDE(p):
    "INSIDE : INSIDE INFO"
    p[0] = p[1] + p[2]
    #p[0] = ""

def p_INSIDE_INFO(p):
    "INSIDE : "
    p[0] = ""

def p_DECL_INT(p):
    "DECL : INT ID"
    if (p[2] in parser.ints.keys()):
        print("Erro na linha ", parser.lines)
        print("A variavel ", p[2], " já existe")
    else:
        parser.ints.update({p[2]: parser.offset_var})
        parser.offset_var += 1
        p[0] = "PUSHI 0\n"

#def p_DECL_STRING(p):
#    "DECL : STRING ID"
#    if (p[2] in parser.strings.keys()):
#        print("Erro na linha ", parser.lines)
#        print("A variavel ", p[2], " já existe")
#    else:
#        parser.strings.update({p[2]: parser.offset_var})
#        parser.offset_var += 1
#        p[0] = "PUSHS NULL\n"

def p_DECL_MATH(p):
    "DECL : INT ID '=' MATH"
    if (p[2] in parser.ints.keys()):
        print("Erro na linha ", parser.lines)
        print("A variavel " + p[1] + " " + p[2], " já existe")
    else:
        parser.ints.update({p[2]: parser.offset_var})
        parser.offset_var += 1
        p[0] = p[4]

#def p_DECL_STRINGS(p):
#    "DECL : STRING ID '=' STRINGS"
#    if (p[2] in parser.strings.keys()):
#        print("Erro na linha ", parser.lines)
#        print("A variavel " + p[1] + " " + p[2], " já existe")
#    else:
#        parser.strings.update({p[2]: parser.offset_var})
#        parser.offset_var += 1
#        p[0] = "PUSHS " + p[4] + "\n"

#def p_DECLA(p):
#    "DECLA : INT ID '[' MATH ']'"
#    if (p[2] in parser.arrays.keys()):
#        print("Erro na linha ", parser.lines)
#        print("A variavel ", p[2], " já existe")
#    else:
#        parser.arrays.update({p[2]: [parser.offset_var,parser.offset_var+int(p[4])-1]})
#        parser.offset_var += int(p[4])
#        p[0] = "CICLO" + str(parser.var_cicle) + ":\n" + p[7] + "NOT\nJZ FIMCICLO" + str(parser.var_cicle) + "\n" + p[3] + "JUMP CICLO" + str(parser.var_cicle) + "\n" + "FIMCICLO" + str(parser.var_cicle) +":\n"
#        "PUSHN "+p[4]+"\n"

def p_INFO_ATUL(p):
    "INFO : ATUL ';'"
    p[0] = p[1]

def p_INFO_IFBLOCK(p):
    "INFO : IFBLOCK"
    p[0] = p[1]

def p_INFO_REPEATBLOCK(p):
    "INFO : REPEATBLOCK"
    p[0] = p[1]

def p_INFO_PRINTM(p):
    "INFO : PRINT '(' MATH ')' ';'"
    p[0] = p[3] + "WRITEI\n"

def p_INFO_PRINTS(p):
    "INFO : PRINT '(' STRINGS ')' ';'"
    p[0] = "PUSHS " + p[3] + "\nWRITES\n"

def p_INFO_RETURN(p):
    "INFO : RETURN MATH ';'"
    p[0] = p[2] + "STOREL -1\nRETURN\n"

#def p_INFO_RETURN(p):
#    "INFO : RETURN ';'"
#    p[0] = "RETURN\n"
#
def p_INFO_COMENTARIO(p):
    "INFO : COMENTARIO"
    p[0] = ""

def p_ATUL_MATH(p):
    "ATUL : ID '=' MATH"
    if (p[1] not in parser.ints.keys()):
        print("Erro na linha ", parser.lines)
        print("A variavel ", p[1], " não existe")
    else:
        p[0] = p[3] + "STOREG " + str(parser.ints.get(p[1])) + "\n"

#def p_ATUL_STRINGS(p):
#    "ATUL : ID '=' STRINGS"
#    if (p[1] not in parser.strings.keys()):
#        print("Erro na linha ", parser.lines)
#        print("A variavel ", p[1], " não existe")
#
#    else:
#        p[0] = p[3] + "STOREG " + str(parser.strings.get(p[1])) + "\n"

#def p_ATUL_ARRAY(p):
#    "ATUL : ID '[' MATH ']' '=' MATH"
#    if (p[1] not in parser.arrays.keys()):
#        print("Erro na linha ", parser.lines)
#        print("A variavel ", p[1], " não existe")
#    else:
#        p[0] = "PUSHGP\n" + "PUSHI " + str(parser.arrays.get(p[1])[0]) + "\nPADD\n" + p[3] + p[6] + "STOREN\n"

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

def p_TERMO_MOD(p):
    "TERMO : TERMO '%' FACTOR"
    p[0] = p[1] + p[3] + "MOD" + "\n"

def p_TERMO_FACTOR(p):
    "TERMO : FACTOR"
    p[0] = p[1]

def p_FACTOR_MATH(p):
    "FACTOR : '(' MATH ')'"
    p[0] = p[2]

def p_FACTOR_NUM(p):
    "FACTOR : NUM"
    p[0] = "PUSHI " + p[1] + "\n"

def p_FACTOR_NUMNEG(p):
    "FACTOR : NUMNEG"
    p[0] = "PUSHI " + p[1].replace('(','').replace(')','') + "\n"

def p_FACTOR_ID(p):
    "FACTOR : ID"
    if(p[1] not in parser.ints.keys()):
        print("Erro na linha ", parser.lines)
        print("A variavel ", p[1], " não existe")
    else:
        res = parser.ints.get(p[1])
        p[0] = "PUSHG " + str(res) + "\n"

def p_FACTOR_FUNC(p):
    "FACTOR : ID '(' ')'"
    if(p[1] not in parser.func):
        print("Erro na linha ", parser.lines)
        print("A funcao ", p[1], " não existe")
    else:
        p[0] = "PUSHI 0\nPUSHA " + p[1] + "\n" + "CALL\n"

#def p_FACTOR_ARRAY(p):
#    "FACTOR : ID '[' MATH ']'"
#    if (p[1] not in parser.arrays.keys()):
#        print("Erro na linha ", parser.lines)
#        print("A variavel ", p[1], " não existe")
#    else:
#        p[0] = "PUSHGP\n" + "PUSHI " + str(parser.arrays.get(p[1])[0]) + "\nPADD\n" + p[3]

def p_FACTOR_READ(p):
    "FACTOR : READ '(' ')'"
    p[0] = "READ\nATOI\n"

def p_IFBLOCK(p):
    "IFBLOCK : IF '(' COND ')' '{' INSIDE '}' IFBLOCK2"
    if(re.match(r"ELIF\d:(.|\n)+",p[8])):
        p[0] = p[3] + "JZ ELIF" + str(parser.var_elif-1) + "\n" + p[6] + "JUMP FIMIF" + str(parser.var_fimif) + "\n" + p[8] + "FIMIF" + str(parser.var_fimif) + ":\n"
    elif(re.match(r"ELSE\d:(.|\n)+",p[8])):
        p[0] = p[3] + "JZ ELSE" + str(parser.var_else-1) + "\n" + p[6] + "JUMP FIMIF" + str(parser.var_fimif) + "\n" + p[8] + "FIMIF" + str(parser.var_fimif) + ":\n"
    else:
        p[0] = p[3] + "JZ FIMIF" + str(parser.var_fimif) + "\n" + p[6] + "FIMIF" + str(parser.var_fimif) + ":\n"
    parser.var_fimif += 1

def p_IFBLOCK2_ELIF(p):
    "IFBLOCK2 : ELIF '(' COND ')' '{' INSIDE '}' IFBLOCK2"
    if(re.match(r"ELIF\d:(.|\n)+",p[8])):
        p[0] = "ELIF" + str(parser.var_elif) + ":\n" + p[3] + "JZ ELIF" + str(parser.var_elif-1) + "\n" + p[6] + "JUMP FIMIF" + str(parser.var_fimif) + "\n" + p[8]
    elif(re.match(r"ELSE\d:(.|\n)+",p[8])):
        p[0] = "ELIF" + str(parser.var_elif) + ":\n" + p[3] + "JZ ELSE" + str(parser.var_else-1) + "\n" + p[6] + "JUMP FIMIF" + str(parser.var_fimif) + "\n" + p[8]
    else:
        p[0] = "ELIF" + str(parser.var_elif) + ":\n" + p[3] + "JZ FIMIF" + str(parser.var_fimif) + "\n" + p[6]
    parser.var_elif+=1

def p_IFBLOCK2_ELSE(p):
    "IFBLOCK2 : ELSE '{' INSIDE '}'"
    p[0] = "ELSE" + str(parser.var_else) +":\n" + p[3]
    parser.var_else += 1

def p_IFBLOCK2_VAZIO(p):
    "IFBLOCK2 : "
    p[0] = ""

def p_REPEATBLOCK(p):
    "REPEATBLOCK : REPEAT '{' INSIDE '}' UNTIL '(' COND ')'"
    p[0] = "CICLO" + str(parser.var_cicle) + ":\n" + p[7] + "NOT\nJZ FIMCICLO" + str(parser.var_cicle) + "\n" + p[3] + "JUMP CICLO" + str(parser.var_cicle) + "\n" + "FIMCICLO" + str(parser.var_cicle) +":\n"
    parser.var_cicle+=1

def p_COND_AND(p):
    "COND : COND '&' '&' COND1"
    p[0] = p[1] + p[4] + "MUL\n"

def p_COND_COND1(p):
    "COND : COND1"
    p[0] = p[1]

def p_COND1_OR(p):
    "COND1 : COND1 '|' '|' COND2"
    p[0] = p[1] + p[4] + "ADD\n"

def p_COND1_COND2(p):
    "COND1 : COND2"
    p[0] = p[1]

def p_COND2_NOT(p):
    "COND2 : NOT COND"
    p[0] = p[2] + "NOT\n"

def p_COND2_TRUE(p):
    "COND2 : TRUE"
    p[0] = "PUSHI 1\n"

def p_COND2_FALSE(p):
    "COND2 : FALSE"
    p[0] = "PUSHI 0\n"

def p_COND2_COND(p):
    "COND2 : '(' COND ')'"
    p[0] = p[2]

def p_COND2_COND3(p):
    "COND2 : COND3"
    p[0] = p[1]

def p_COND3_MENOR(p):
    "COND3 : MATH '<' MATH"
    p[0] = p[1] + p[3] + "INF\n"

def p_COND3_MAIOR(p):
    "COND3 : MATH '>' MATH"
    p[0] = p[1] + p[3] + "SUP\n"
    
def p_COND3_IGUAL(p):
    "COND3 : MATH '=' '=' MATH"
    p[0] = p[1] + p[4] + "EQUAL\n"
    
def p_COND3_DIF(p):
    "COND3 : MATH '!' '=' MATH"
    p[0] = p[1] + p[4] + "EQUAL\nNOT\n"
    
def p_COND3_MAIORI(p):
    "COND3 : MATH '<' '=' MATH"
    p[0] = p[1] + p[4] + "INFEQ\n"
    
def p_COND3_MENORI(p):
    "COND3 : MATH '>' '=' MATH"
    p[0] = p[1] + p[4] + "SEQ\n"
    
def p_COND3_MATH(p):
    "COND3 : MATH"
    p[0] = p[1]
    
#def p_COND1_OR(p):
#    "COND1 : '|' '|' COND"
#    p[0] = p[3] + "ADD\n"
#
#def p_COND1_AND(p):
#    "COND1 : '&' '&' COND"
#    p[0] = p[3] + "MUL\n"
#
#def p_COND1_VAZIO(p):
#    "COND1 : "
#    p[0] = ""


def p_error(p):
    print(p)
    print("Syntax error in input!")

#Build the parser
parser = yacc.yacc()

#My state
parser.ints = {}
parser.strings = {}
#parser.arrays = {}
parser.func = []
parser.current_func = ""
parser.offset_var = 0
parser.var_elif = 0
parser.var_else = 0
parser.var_fimif = 0
parser.var_cicle = 0
parser.lines = 1

#Read line input and parse it

f = open("trial.c", "r").read()
#f = open(sys.argv[1], "r").read()
#txt = f.split("\n")
#print(txt)
#for linha in txt:
#    result = lexer.token()
#    print(result)
parser.parse(f)
