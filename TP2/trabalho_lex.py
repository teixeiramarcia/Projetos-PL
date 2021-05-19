import ply.lex as lex

tokens = ['INT', 'ID', 'IF', 'ELSE', 'ELIF', 'REPEAT', 'READ', 'PRINT', 'NUM', 'RETURN'] 
literals = ['(', ')',';','<','>','=','+','-','*','/','{','}','[',']','|','&']

def t_IF(t):
    r'if'

def t_ELIF(t):
    r'elif'

def t_ELSE(t):
    r'else'

def t_REPEAT(t):
    r'repeat'

def t_RETURN(t):
    r'return'

def t_READ(t):
    r'scan'

def t_PRINT(t):
    r'print'

def t_INT(t):
    r'int'

def t_NUM(t):
    r'\d+'

def t_ID(t):
    r'[a-z][a-zA-Z0-9]*'

t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

#Build the Lexer
lexer = lex.lex()