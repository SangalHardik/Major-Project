import ply.lex as lex
reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'cin': 'CIN',
    'cout': 'COUT',
    'else if': 'ELSEIF',
    'operator': 'OPERATOR',
    'identifier': 'IDENTIFIER'
}

tokens = [
    'EQUALS',
    'ID',
    'STRING',
    'LCURLY',
    'RCURLY',
    'LPAR',
    'RPAR',
    'SEMICOLON',
    'LEFTSHIFT',
    'RIGHTSHIFT',
    'GREATER',
    'LESS',
    'INCREMENT',
    'DECREMENT',
    'PLUSEQUAL',
    'MINUSEQUAL',
    'DOUBLE_EQUALS',
    'PLUS',
    'MINUS'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_EQUALS = r'\='
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LPAR = r'\('
t_RPAR = r'\)'
t_SEMICOLON = r';'
t_GREATER = r'>'
t_LESS = r'<'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_DOUBLE_EQUALS = r'=='
t_PLUS = r'\+'
t_MINUS = r'-'

# Ignore whitespace
t_ignore = '\t '

def t_IDENTIFIER(t):
    r'int|string|char|bool|float'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    print(t.value, "t_IDENTIFIER reached")
    return t

def t_OPERATOR(t):
    r'&&|(\|\|)'
    t.type = reserved.get(t.value, 'OPERATOR')
    return t

def t_ID(t):
    r'(if|else|then|while|for|cin|cout)'
    print(t.value, "t_ID reached")
    if t.value in reserved:
        t.type = reserved.get(t.value, 'STRING')
        return t
    else:
        return t

def t_LEFTSHIFT(t):
    r'<<'
    t.type = reserved.get(t.value, 'LEFTSHIFT')
    return t

def t_RIGHTSHIFT(t):
    r'>>'
    t.type = reserved.get(t.value, 'RIGHTSHIFT')
    return t

def t_STRING(t):
    r'[a-zA-Z_0-9"<>=+ ][a-zA-Z_=*+-/_0-9"<>=+ ]*'
    if t.value in reserved:
        t.type = reserved.get(t.value, 'STRING')
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    print('t.lexer.lineno : ', t.lexer.lineno)

def t_error(t):
    print("Illegal characters!", t)
    t.lexer.skip(1)

def t_COMMENT(t):
    r'\//.*'
    pass
    # No return value. Token discarded

# Build the lexer
def build_lexer():
    lexer = lex.lex()
    return lexer