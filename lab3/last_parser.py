import scanner
import AST
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    ('left', '='),
    ('nonassoc', '<', '>', 'LE', 'GE'),
    ("left", '+', '-'),
    ("left", "*", "/"),
    ("left", 'M_ADD', 'M_SUB'),
    ("left", "M_MUL", "M_DIV"),
    ('right', 'UMINUS'),
    ("left", "M_TRANSPOSE"),
    ("nonassoc", "IFX"),
    ("nonassoc", "ELSE")
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(t):
    """program : instructions"""
    t[1] = AST.Instructions(t[1])
    t[0] = AST.Program(t[1])


def p_instructions(t):
    """instructions : instructions instruction
                | """
    if len(t) > 1:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = []


def p_empty_instruction(t):
    """instruction : ';'"""


def p_expression_value(t):
    """expression : INT
                  | FLOAT
                  | matrix
                  | STRING"""
    if type(t[1]) == int:
        t[0] = AST.IntNum(t[1])
    elif type(t[1]) == float:
        t[0] = AST.FloatNum(t[1])
    elif type(t[1]) == str:
        t[0] = AST.String(t[1])
    elif type(t[1]) == list:
        t[0] = AST.Vector(t[1])
    else:
        t[0] = t[1]
    # # else:
    # #     print(t[1])


def p_expression_ID(t):
    """expression : ID"""

    t[0] = AST.Variable(t[1])


def p_expression_gr(t):
    """expression : '(' expression ')'"""
    t[0] = t[2]


def p_instruction_scope(t):
    """instruction : '{' instructions '}'"""
    t[0] = t[2]  # nie wiem czy dobrze


def p_expression_binop(t):
    """expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression"""
    t[0] = AST.BinExpr(t[2], t[1], t[3])


def p_expression_binop_matrix(t):
    """expression : expression M_ADD expression
                  | expression M_SUB expression
                  | expression M_MUL expression
                  | expression M_DIV expression"""
    t[0] = AST.BinExpr(t[2], t[1], t[3])


def p_expression_relation(t):
    """condition : expression '<' expression
                | expression '>' expression
                | expression LE expression
                | expression GE expression
                | expression NEQ expression
                | expression EQ expression"""
    t[0] = AST.RelExpr(t[2], t[1], t[3])


def p_uminus(t):
    """expression : '-' expression %prec UMINUS"""
    t[0] = AST.UMinus(t[2])


def p_transpose(t):
    """matrix : expression M_TRANSPOSE"""
    t[0] = AST.Transpose(t[1])


def p_matrix_generator(t):
    """matrix : ZEROS '(' expression ')'
              | ONES '(' expression ')'
              | EYE '(' expression ')'"""
    t[0] = AST.MatrixFunc(t[1], (t[3],))
    #print(type(t[0]))


def p_assignment(t):
    """instruction : ID '=' expression ';'
                    | ID A_ADD expression ';'
                    | ID A_SUB expression ';'
                    | ID A_MUL expression ';'
                    | ID A_DIV expression ';'"""
    t[0] = AST.Assign(t[2], AST.Variable(t[1]), t[3])


def p_position_assignment(t):
    """instruction : ID array '=' expression ';'
                   | ID array A_ADD expression ';'
                   | ID array A_SUB expression ';'
                   | ID array A_MUL expression ';'
                   | ID array A_DIV expression ';'"""  # A[0,1] = 5, etc.

    t[0] = AST.Assign(t[3], AST.Ref(t[1], t[2]), t[4])


def p_if_else(t):
    """instruction : IF '(' condition ')' instruction %prec IFX
                  | IF '(' condition ')' instruction ELSE instruction"""
    if len(t) == 6:
        t[0] = AST.If(t[3], t[5])
    else:
        t[0] = AST.If(t[3], t[5], t[7])


def p_while(t):
    """instruction : WHILE '(' condition ')' instruction"""
    t[0] = AST.While(t[3], t[5])


def p_for(t):
    """instruction : FOR ID '=' expression ':' expression instruction"""
    x = AST.Range(t[4], t[6])
    t[0] = AST.For(AST.Variable(t[2]), x, t[7])


def p_special_instruction(t):
    """instruction : BREAK ';'
                   | CONTINUE ';'
                   | RETURN expression ';'"""
    if t[1] == 'break':
        t[0] = AST.Break()
    elif t[1] == 'continue':
        t[0] = AST.Continue()
    else:
        t[0] = AST.Return(t[2])


def p_print(t): #args???
    """instruction : PRINT list ';'"""
    t[0] = AST.Print(AST.Args(t[2]))


def p_matrix(t):
    """matrix : '[' arraylist ']'"""
    t[0] = t[2]


def p_arraylist(t):
    """arraylist : array
                 | arraylist ',' array"""
    if len(t) > 2:
        for arr in t[1]:
            if len(arr) != len(t[3]):
                raise SyntaxError
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]


def p_array(t):
    """array : '[' list ']'"""
    for i in t[2]:
        if not isinstance(i, int) and not isinstance(i, float):
            raise SyntaxError
    t[0] = t[2]


def p_list(t):
    """list : expression
            | list ',' expression"""
    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]


def p_array_access(t):
    """expression : ID array"""
    t[0] = AST.Ref(t[1], t[2])


parser = yacc.yacc()

if __name__ == '__main__':
    while True:
        try:
            s = input('> > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result)
