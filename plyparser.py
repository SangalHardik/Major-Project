import ply.yacc as yacc
import timeit
from plytoken import *

# ----------------------------------------------------------------------------------------------
# parser yacc part

print_status_p = False


def p_statement(p):
    '''
    statement : s1 s2
            | empty
    '''

    try:
        if (p[2] == None):
            p[0] = [p[1]]
        else:
            p[0] = [p[1], p[2]]

        if (print_status_p):
            print("P_STATEMENT : ", p[0])
    except IndexError:
        pass


def p_s1(p):
    '''
    s1 : var_declaration_statement
          | if_expression
          | io_statement
          | loop_expression
          | STRING SEMICOLON
          | empty
    '''
    p[0] = p[1]

    if (print_status_p):
        print("p_s1 : ", p[0])


def p_s2(p):
    '''
    s2 : statement
    '''
    p[0] = p[1]

    if (print_status_p):
        print("p_s2 : ", p[0])


def p_io_statement(p):
    '''
    io_statement : CIN RIGHTSHIFT STRING SEMICOLON
                 | COUT LEFTSHIFT STRING SEMICOLON
    '''

    p[0] = (p[1], p[2], p[3], p[4])

    if (print_status_p):
        print("IO STATEMENT : ", p[0])


def p_var_declaration_statement(p):
    '''
    var_declaration_statement : IDENTIFIER STRING SEMICOLON
    '''

    p[0] = (p[1], p[2], p[3])

    if (print_status_p):
        print("VAR DECLARATION : ", p[0])


def p_loop_expression(p):
    '''
    loop_expression : WHILE condition LCURLY statement RCURLY
                    | FOR forcondition LCURLY statement RCURLY
    '''

    p[0] = (p[1], p[2], p[3], p[4], p[5])

    if (print_status_p):
        print("Loop Expression", p[0])


def p_condition(p):
    '''
    condition : LPAR expression RPAR
    '''
    p[0] = ("CONDITION", p[1], p[2], p[3])

    if (print_status_p):
        print("CONDITION ", p[0])


def p_forcondition(p):
    '''
    forcondition : LPAR expression SEMICOLON expression SEMICOLON expression RPAR
                | LPAR IDENTIFIER expression SEMICOLON expression SEMICOLON expression RPAR
    '''
    if len(p) == 9 and p[2] == 'IDENTIFIER':
        # Handle declaration in for loop (e.g., for(int i=0; i<10; i++))
        p[0] = ("FOR CONDITION", p[1], f"{p[2]} {p[3]}; {p[5]}; {p[7]}", p[8])
    else:
        # Handle standard for loop (e.g., for(i=0; i<10; i++))
        p[0] = ("FOR CONDITION", p[1], f"{p[2]}; {p[4]}; {p[6]}", p[7])

    if (print_status_p):
        print("FOR CONDITION ", p[0])


def p_if_expression(p):
    '''
    if_expression : IF condition LCURLY statement RCURLY else_expression
                | IF condition LCURLY statement RCURLY elseif_expression
    '''
    if str.lower(p[1]) == 'if':
        if (p[6] == None):
            p[0] = (p[1], p[2], p[3], p[4], p[5])
        else:
            p[0] = (p[1], p[2], p[3], p[4], p[5], [p[6]])
    else:
        p[0] = p[1]

    if (print_status_p):
        print("IF EXPRESSION ", p[0])


def p_elseif_expression(p):
    '''
    elseif_expression : ELSE IF condition LCURLY statement RCURLY elseif_expression
                        | ELSE IF condition LCURLY statement RCURLY else_expression
                      | empty
    '''

    try:
        if str.lower(p[1]) == 'else' and str.lower(p[2]) == 'if':
            if (p[7] == None):
                p[0] = ("ELSE IF", p[3], p[4], p[5], p[6])
            else:
                p[0] = ("ELSE IF", p[3], p[4], p[5], p[6], [p[7]])
        else:
            p[0] = p[1]

        if (print_status_p):
            print("ELSE IF EXPRESSION", p[0], "\n")

    except:
        pass


def p_else_expression(p):
    '''
    else_expression : ELSE LCURLY statement RCURLY
                    | empty
    '''

    try:
        if str.lower(p[1]) == 'else':
            p[0] = (p[1], p[2], p[3], p[4])
        else:
            p[0] = p[1]

        if (print_status_p):
            print("ELSE EXPRESSION", p[0])
    except:
        pass


def p_expression_string_id(p):
    '''
    expression : STRING
               | ID
               | empty

    '''
    p[0] = p[1]

    if (print_status_p):
        print("EXPRESSION STRING ID", p[0])


# Passes Empty
def p_empty(p):
    'empty : '
    pass


error_logger = []
def p_error(p):
    global error_logger

    print("Syntax error at line ", str(p))
    error_logger.append("Syntax error at line "+ str(p))

    return error_logger


def testToken(code):
    lexer = build_lexer()
    lexer.input(code)
    while True:
        tok = lexer.token()
        if not tok:
            break

        print("token : ",tok)

    return lexer

def create_new_parser():
    error_logger.clear()
    parser = yacc.yacc(errorlog=yacc.NullLogger())

    return parser