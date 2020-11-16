import ply.yacc as yacc
import numpy as np
import scanner

tokens = scanner.tokens
env = {}


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


precedence = (
    ('nonassoc', '<', '>', 'LE', 'GE', 'EQ', 'NEQ'),
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS')
)


def p_program(p):
    """program : instructions_opt"""


def p_instructions_opt_1(p):
    """instructions_opt : instructions """


def p_instructions_opt_2(p):
    """instructions_opt : """


def p_instructions_1(p):
    """instructions : instructions instruction """


def p_instructions_2(p):
    """instructions : instruction """


def p_expression(p):
    """expresion : ID"""


def p_instruction_assign(p):
    """instruction : ID '=' expression ';'
                   | ID A_ADD expression ';'
                   | ID A_SUB expression ';'
                   | ID A_MUL expression ';'
                   | ID A_DIV expression ';'"""

    if p[2] == '=':
        env[p[1]] = p[3]
    elif p[1] not in env:
        raise SyntaxError
    elif p[2] == '+=':
        p[1] += p[3]
    elif p[2] == '-=':
        p[1] -= p[3]
    elif p[2] == '*=':
        p[1] *= p[3]
    elif p[2] == '/=':
        p[1] /= p[3]


def p_instruction_assign_matrix(p):
    """instruction : ID '=' matrix ';'
                   | ID A_ADD matrix ';'
                   | ID A_SUB matrix ';'
                   | ID A_MUL matrix ';'
                   | ID A_DIV matrix ';' """
    try:
        if p[2] == '=':
            env[p[1]] = p[3]
        elif p[1] not in env:
            raise SyntaxError
        elif p[2] == '+=':
            p[1] += p[3]
        elif p[2] == '-=':
            p[1] -= p[3]
        elif p[2] == '*=':
            p[1] *= p[3]
        elif p[2] == '/=':
            p[1] /= p[3]

    except ValueError:
        raise SyntaxError


def p_expression_binary_operation(p):
    """expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression """

    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_matrix_binary_operation(p):
    """matrix : matrix '+' matrix
                  | matrix '-' matrix
                  | matrix '*' matrix
                  | matrix '/' matrix """
    try:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    except ValueError:
        raise SyntaxError


def p_expression_relation(p):
    """bool : expression '>' expression
            | expression '<' expression
            | expression LE expression
            | expression GE expression
            | expression EQ expression
            | expression NEQ expression """

    if p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]


def p_expression_uminus(p):
    """expression : '-' expression %prec UMINUS"""
    p[0] = -p[2]


def p_matrix_uminus(p):
    """matrix : '-' matrix %prec UMINUS"""
    p[0] = -p[2]


def p_matrix_transpose(p):
    """matrix : matrix TRANSPOSE"""
    p[0] = p[1].T


def p_matrix(p):
    """matrix : '[' arraylist ']'"""
    p[0] = np.asarray(p[2])


def p_arraylist_1(t):
    """arraylist : array"""
    t[0] = [t[1]]


def p_arraylist_2(p):
    """arraylist : array ',' arraylist"""
    p[0] = [p[1]] + p[3]


def p_array(t):
    """array : '[' list ']'"""
    t[0] = t[2]


def p_list_1(t):
    """list : expression"""
    t[0] = [t[1]]


def p_list_2(p):
    """list : expression COMMA list"""
    p[0] = [p[1]] + p[3]


def p_expression_no(p):
    """expression : INT
                  | FLOAT"""
    p[0] = p[1]


def p_matrix_function(p):
    """matrix : ZEROS '(' expression ')'
              | ONES '(' expression ')'
              | EYE '(' expression ')' """
    if p[1] == 'zeros':
        p[0] = np.zeros(p[3])
    elif p[1] == 'ones':
        p[0] = np.ones(p[3])
    elif p[1] == 'eye':
        p[0] = np.eye(p[3])


def p_matrix_acess(p):
    """instruction : ID array '=' expression ';'"""
    try:
        env[p[1]][p[2][0]][p[2][1]] = p[4]
    except:                                                     # dopisac errory
        raise SyntaxError


parser = yacc.yacc()
