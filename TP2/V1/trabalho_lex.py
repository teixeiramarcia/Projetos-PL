import ply.lex as lex

tokens = ['INT', 'ID', 'IF', 'ELSE', 'ELIF', 'REPEAT', 'READ', 'PRINT', 'NUM', 'NUMNEG', 'RETURN', 'COMENTARIO', 'NOT', 'TRUE', 'FALSE', 'UNTIL', 'MAIN', 'STRINGS']
literals = ['(', ')',';','<','>','=','+','-','*','/','{','}','[',']','|','&','!', '%']

def t_IF(t):
    r'if'
    return t

def t_ELIF(t):
    r'elif'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_UNTIL(t):
    r'until'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_READ(t):
    r'read'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_INT(t):
    r'int'
    return t

def t_MAIN(t):
    r'main'
    return t

def t_NOT(t):
    r'not'
    return t

def t_TRUE(t):
    r'TRUE'
    return t

def t_FALSE(t):
    r'FALSE'
    return t

def t_NUMNEG(t):
    r'\(-\d+\)'
    return t

def t_NUM(t):
    r'\d+'
    return t

def t_STRINGS(t):
    r'"[^"]*"'
    return t

def t_ID(t):
    r'[a-z][a-zA-Z0-9]*'
    return t

def t_COMENTARIO(t):
    r'(\/\/.+)|(/\*((?!\*/).|\n)*\*/)'
    return t


t_ignore = " \t\n\r"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

#Build the Lexer
lexer = lex.lex()