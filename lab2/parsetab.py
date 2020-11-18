
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left=nonassoc<>LEGEleft+-left*/leftM_ADDM_SUBleftM_MULM_DIVrightUMINUSleftM_TRANSPOSEnonassocIFXnonassocELSEA_ADD A_DIV A_MUL A_SUB BREAK CONTINUE ELSE EQ EYE FLOAT FOR GE ID IF INT LE M_ADD M_DIV M_MUL M_SUB M_TRANSPOSE NEQ ONES PRINT RETURN STRING WHILE ZEROSprogram : instructionsinstructions : instructions instruction\n                | instruction : ';'expression : INT\n                  | FLOAT\n                  | matrix\n                  | STRINGexpression : IDexpression : '(' expression ')'instruction : '{' instructions '}'expression : expression '+' expression\n                  | expression '-' expression\n                  | expression '*' expression\n                  | expression '/' expressionexpression : expression M_ADD expression\n                  | expression M_SUB expression\n                  | expression M_MUL expression\n                  | expression M_DIV expressioncondition : expression '<' expression\n                | expression '>' expression\n                | expression LE expression\n                | expression GE expression\n                | expression NEQ expression\n                | expression EQ expressionexpression : '-' expression %prec UMINUSmatrix : expression M_TRANSPOSEmatrix : ZEROS '(' expression ')'\n              | ONES '(' expression ')'\n              | EYE '(' expression ')'instruction : ID '=' expression ';'\n                    | ID A_ADD expression ';'\n                    | ID A_SUB expression ';'\n                    | ID A_MUL expression ';'\n                    | ID A_DIV expression ';'instruction : ID array '=' expression ';'\n                   | ID array A_ADD expression ';'\n                   | ID array A_SUB expression ';'\n                   | ID array A_MUL expression ';'\n                   | ID array A_DIV expression ';'instruction : IF '(' condition ')' instruction %prec IFX\n                  | IF '(' condition ')' instruction ELSE instructioninstruction : WHILE '(' condition ')' instructioninstruction : FOR ID '=' expression ':' expression instructioninstruction : BREAK ';'\n                   | CONTINUE ';'\n                   | RETURN expression ';'instruction : PRINT list ';'matrix : '[' arraylist ']'arraylist : array\n                 | arraylist ',' arrayarray : '[' list ']'list : expression\n            | list ',' expressionexpression : ID array"
    
_lr_action_items = {';':([0,2,3,4,5,10,11,14,25,26,27,28,29,30,31,32,39,40,41,42,43,44,45,46,57,66,67,69,75,77,78,79,80,81,82,83,84,85,86,87,88,95,97,98,99,100,101,102,103,104,105,109,111,112,113,114,115,116,117,124,126,127,128,130,131,132,133,],[-3,4,-2,-4,-3,25,26,4,-45,-46,57,-5,-6,-7,-8,-9,75,-53,-11,77,78,79,80,81,-47,-27,-55,-26,-48,-31,-32,-33,-34,-35,112,113,114,115,116,-52,4,4,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-54,-36,-37,-38,-39,-40,-41,-43,-28,-29,-30,4,4,-42,-44,]),'{':([0,2,3,4,5,14,25,26,28,29,30,31,32,41,57,66,67,69,75,77,78,79,80,81,87,88,95,97,98,99,100,101,102,103,104,105,109,112,113,114,115,116,117,124,126,127,128,130,131,132,133,],[-3,5,-2,-4,-3,5,-45,-46,-5,-6,-7,-8,-9,-11,-47,-27,-55,-26,-48,-31,-32,-33,-34,-35,-52,5,5,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-36,-37,-38,-39,-40,-41,-43,-28,-29,-30,5,5,-42,-44,]),'ID':([0,2,3,4,5,9,12,13,14,15,16,17,18,19,21,22,23,25,26,28,29,30,31,32,33,34,41,47,48,49,50,51,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,72,75,76,77,78,79,80,81,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,103,104,105,109,112,113,114,115,116,117,124,125,126,127,128,130,131,132,133,],[-3,6,-2,-4,-3,24,32,32,6,32,32,32,32,32,32,32,32,-45,-46,-5,-6,-7,-8,-9,32,32,-11,32,32,32,32,32,32,-47,32,32,32,32,32,32,32,32,-27,-55,-26,32,32,32,-48,32,-31,-32,-33,-34,-35,-52,6,32,32,32,32,32,32,6,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-36,-37,-38,-39,-40,-41,-43,32,-28,-29,-30,6,6,-42,-44,]),'IF':([0,2,3,4,5,14,25,26,28,29,30,31,32,41,57,66,67,69,75,77,78,79,80,81,87,88,95,97,98,99,100,101,102,103,104,105,109,112,113,114,115,116,117,124,126,127,128,130,131,132,133,],[-3,7,-2,-4,-3,7,-45,-46,-5,-6,-7,-8,-9,-11,-47,-27,-55,-26,-48,-31,-32,-33,-34,-35,-52,7,7,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-36,-37,-38,-39,-40,-41,-43,-28,-29,-30,7,7,-42,-44,]),'WHILE':([0,2,3,4,5,14,25,26,28,29,30,31,32,41,57,66,67,69,75,77,78,79,80,81,87,88,95,97,98,99,100,101,102,103,104,105,109,112,113,114,115,116,117,124,126,127,128,130,131,132,133,],[-3,8,-2,-4,-3,8,-45,-46,-5,-6,-7,-8,-9,-11,-47,-27,-55,-26,-48,-31,-32,-33,-34,-35,-52,8,8,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-36,-37,-38,-39,-40,-41,-43,-28,-29,-30,8,8,-42,-44,]),'FOR':([0,2,3,4,5,14,25,26,28,29,30,31,32,41,57,66,67,69,75,77,78,79,80,81,87,88,95,97,98,99,100,101,102,103,104,105,109,112,113,114,115,116,117,124,126,127,128,130,131,132,133,],[-3,9,-2,-4,-3,9,-45,-46,-5,-6,-7,-8,-9,-11,-47,-27,-55,-26,-48,-31,-32,-33,-34,-35,-52,9,9,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-36,-37,-38,-39,-40,-41,-43,-28,-29,-30,9,9,-42,-44,]),'BREAK':([0,2,3,4,5,14,25,26,28,29,30,31,32,41,57,66,67,69,75,77,78,79,80,81,87,88,95,97,98,99,100,101,102,103,104,105,109,112,113,114,115,116,117,124,126,127,128,130,131,132,133,],[-3,10,-2,-4,-3,10,-45,-46,-5,-6,-7,-8,-9,-11,-47,-27,-55,-26,-48,-31,-32,-33,-34,-35,-52,10,10,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-36,-37,-38,-39,-40,-41,-43,-28,-29,-30,10,10,-42,-44,]),'CONTINUE':([0,2,3,4,5,14,25,26,28,29,30,31,32,41,57,66,67,69,75,77,78,79,80,81,87,88,95,97,98,99,100,101,102,103,104,105,109,112,113,114,115,116,117,124,126,127,128,130,131,132,133,],[-3,11,-2,-4,-3,11,-45,-46,-5,-6,-7,-8,-9,-11,-47,-27,-55,-26,-48,-31,-32,-33,-34,-35,-52,11,11,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-36,-37,-38,-39,-40,-41,-43,-28,-29,-30,11,11,-42,-44,]),'RETURN':([0,2,3,4,5,14,25,26,28,29,30,31,32,41,57,66,67,69,75,77,78,79,80,81,87,88,95,97,98,99,100,101,102,103,104,105,109,112,113,114,115,116,117,124,126,127,128,130,131,132,133,],[-3,12,-2,-4,-3,12,-45,-46,-5,-6,-7,-8,-9,-11,-47,-27,-55,-26,-48,-31,-32,-33,-34,-35,-52,12,12,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-36,-37,-38,-39,-40,-41,-43,-28,-29,-30,12,12,-42,-44,]),'PRINT':([0,2,3,4,5,14,25,26,28,29,30,31,32,41,57,66,67,69,75,77,78,79,80,81,87,88,95,97,98,99,100,101,102,103,104,105,109,112,113,114,115,116,117,124,126,127,128,130,131,132,133,],[-3,13,-2,-4,-3,13,-45,-46,-5,-6,-7,-8,-9,-11,-47,-27,-55,-26,-48,-31,-32,-33,-34,-35,-52,13,13,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-36,-37,-38,-39,-40,-41,-43,-28,-29,-30,13,13,-42,-44,]),'$end':([0,1,2,3,4,25,26,41,57,75,77,78,79,80,81,112,113,114,115,116,117,124,132,133,],[-3,0,-1,-2,-4,-45,-46,-11,-47,-48,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-43,-42,-44,]),'}':([3,4,5,14,25,26,41,57,75,77,78,79,80,81,112,113,114,115,116,117,124,132,133,],[-2,-4,-3,41,-45,-46,-11,-47,-48,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-43,-42,-44,]),'ELSE':([4,25,26,41,57,75,77,78,79,80,81,112,113,114,115,116,117,124,132,133,],[-4,-45,-46,-11,-47,-48,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,130,-43,-42,-44,]),'=':([6,20,24,87,],[15,47,56,-52,]),'A_ADD':([6,20,87,],[16,48,-52,]),'A_SUB':([6,20,87,],[17,49,-52,]),'A_MUL':([6,20,87,],[18,50,-52,]),'A_DIV':([6,20,87,],[19,51,-52,]),'[':([6,12,13,15,16,17,18,19,21,22,23,32,33,34,38,47,48,49,50,51,56,58,59,60,61,62,63,64,65,70,71,72,76,89,90,91,92,93,94,110,125,],[21,38,38,38,38,38,38,38,38,38,38,21,38,38,21,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,21,38,]),'(':([7,8,12,13,15,16,17,18,19,21,22,23,33,34,35,36,37,47,48,49,50,51,56,58,59,60,61,62,63,64,65,70,71,72,76,89,90,91,92,93,94,125,],[22,23,33,33,33,33,33,33,33,33,33,33,33,33,70,71,72,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'INT':([12,13,15,16,17,18,19,21,22,23,33,34,47,48,49,50,51,56,58,59,60,61,62,63,64,65,70,71,72,76,89,90,91,92,93,94,125,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'FLOAT':([12,13,15,16,17,18,19,21,22,23,33,34,47,48,49,50,51,56,58,59,60,61,62,63,64,65,70,71,72,76,89,90,91,92,93,94,125,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'STRING':([12,13,15,16,17,18,19,21,22,23,33,34,47,48,49,50,51,56,58,59,60,61,62,63,64,65,70,71,72,76,89,90,91,92,93,94,125,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'-':([12,13,15,16,17,18,19,21,22,23,27,28,29,30,31,32,33,34,40,42,43,44,45,46,47,48,49,50,51,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,82,83,84,85,86,87,89,90,91,92,93,94,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,118,119,120,121,122,123,125,126,127,128,131,],[34,34,34,34,34,34,34,34,34,34,59,-5,-6,-7,-8,-9,34,34,59,59,59,59,59,59,34,34,34,34,34,59,34,34,34,34,34,34,34,34,34,-27,-55,59,-26,34,34,34,34,59,59,59,59,59,-52,34,34,34,34,34,34,59,-12,-13,-14,-15,-16,-17,-18,-19,-10,59,59,59,-49,59,59,59,59,59,59,59,34,-28,-29,-30,59,]),'ZEROS':([12,13,15,16,17,18,19,21,22,23,33,34,47,48,49,50,51,56,58,59,60,61,62,63,64,65,70,71,72,76,89,90,91,92,93,94,125,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'ONES':([12,13,15,16,17,18,19,21,22,23,33,34,47,48,49,50,51,56,58,59,60,61,62,63,64,65,70,71,72,76,89,90,91,92,93,94,125,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'EYE':([12,13,15,16,17,18,19,21,22,23,33,34,47,48,49,50,51,56,58,59,60,61,62,63,64,65,70,71,72,76,89,90,91,92,93,94,125,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'+':([27,28,29,30,31,32,40,42,43,44,45,46,54,66,67,68,69,82,83,84,85,86,87,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,118,119,120,121,122,123,126,127,128,131,],[58,-5,-6,-7,-8,-9,58,58,58,58,58,58,58,-27,-55,58,-26,58,58,58,58,58,-52,58,-12,-13,-14,-15,-16,-17,-18,-19,-10,58,58,58,-49,58,58,58,58,58,58,58,-28,-29,-30,58,]),'*':([27,28,29,30,31,32,40,42,43,44,45,46,54,66,67,68,69,82,83,84,85,86,87,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,118,119,120,121,122,123,126,127,128,131,],[60,-5,-6,-7,-8,-9,60,60,60,60,60,60,60,-27,-55,60,-26,60,60,60,60,60,-52,60,60,60,-14,-15,-16,-17,-18,-19,-10,60,60,60,-49,60,60,60,60,60,60,60,-28,-29,-30,60,]),'/':([27,28,29,30,31,32,40,42,43,44,45,46,54,66,67,68,69,82,83,84,85,86,87,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,118,119,120,121,122,123,126,127,128,131,],[61,-5,-6,-7,-8,-9,61,61,61,61,61,61,61,-27,-55,61,-26,61,61,61,61,61,-52,61,61,61,-14,-15,-16,-17,-18,-19,-10,61,61,61,-49,61,61,61,61,61,61,61,-28,-29,-30,61,]),'M_ADD':([27,28,29,30,31,32,40,42,43,44,45,46,54,66,67,68,69,82,83,84,85,86,87,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,118,119,120,121,122,123,126,127,128,131,],[62,-5,-6,-7,-8,-9,62,62,62,62,62,62,62,-27,-55,62,-26,62,62,62,62,62,-52,62,62,62,62,62,-16,-17,-18,-19,-10,62,62,62,-49,62,62,62,62,62,62,62,-28,-29,-30,62,]),'M_SUB':([27,28,29,30,31,32,40,42,43,44,45,46,54,66,67,68,69,82,83,84,85,86,87,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,118,119,120,121,122,123,126,127,128,131,],[63,-5,-6,-7,-8,-9,63,63,63,63,63,63,63,-27,-55,63,-26,63,63,63,63,63,-52,63,63,63,63,63,-16,-17,-18,-19,-10,63,63,63,-49,63,63,63,63,63,63,63,-28,-29,-30,63,]),'M_MUL':([27,28,29,30,31,32,40,42,43,44,45,46,54,66,67,68,69,82,83,84,85,86,87,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,118,119,120,121,122,123,126,127,128,131,],[64,-5,-6,-7,-8,-9,64,64,64,64,64,64,64,-27,-55,64,-26,64,64,64,64,64,-52,64,64,64,64,64,64,64,-18,-19,-10,64,64,64,-49,64,64,64,64,64,64,64,-28,-29,-30,64,]),'M_DIV':([27,28,29,30,31,32,40,42,43,44,45,46,54,66,67,68,69,82,83,84,85,86,87,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,118,119,120,121,122,123,126,127,128,131,],[65,-5,-6,-7,-8,-9,65,65,65,65,65,65,65,-27,-55,65,-26,65,65,65,65,65,-52,65,65,65,65,65,65,65,-18,-19,-10,65,65,65,-49,65,65,65,65,65,65,65,-28,-29,-30,65,]),'M_TRANSPOSE':([27,28,29,30,31,32,40,42,43,44,45,46,54,66,67,68,69,82,83,84,85,86,87,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,118,119,120,121,122,123,126,127,128,131,],[66,-5,-6,-7,-8,-9,66,66,66,66,66,66,66,-27,-55,66,66,66,66,66,66,66,-52,66,66,66,66,66,66,66,66,66,-10,66,66,66,-49,66,66,66,66,66,66,66,-28,-29,-30,66,]),',':([28,29,30,31,32,39,40,52,66,67,69,73,74,87,97,98,99,100,101,102,103,104,105,109,111,126,127,128,129,],[-5,-6,-7,-8,-9,76,-53,76,-27,-55,-26,110,-50,-52,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-54,-28,-29,-30,-51,]),']':([28,29,30,31,32,40,52,66,67,69,73,74,87,97,98,99,100,101,102,103,104,105,109,111,126,127,128,129,],[-5,-6,-7,-8,-9,-53,87,-27,-55,-26,109,-50,-52,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-54,-28,-29,-30,-51,]),'<':([28,29,30,31,32,54,66,67,69,87,97,98,99,100,101,102,103,104,105,109,126,127,128,],[-5,-6,-7,-8,-9,89,-27,-55,-26,-52,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-28,-29,-30,]),'>':([28,29,30,31,32,54,66,67,69,87,97,98,99,100,101,102,103,104,105,109,126,127,128,],[-5,-6,-7,-8,-9,90,-27,-55,-26,-52,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-28,-29,-30,]),'LE':([28,29,30,31,32,54,66,67,69,87,97,98,99,100,101,102,103,104,105,109,126,127,128,],[-5,-6,-7,-8,-9,91,-27,-55,-26,-52,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-28,-29,-30,]),'GE':([28,29,30,31,32,54,66,67,69,87,97,98,99,100,101,102,103,104,105,109,126,127,128,],[-5,-6,-7,-8,-9,92,-27,-55,-26,-52,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-28,-29,-30,]),'NEQ':([28,29,30,31,32,54,66,67,69,87,97,98,99,100,101,102,103,104,105,109,126,127,128,],[-5,-6,-7,-8,-9,93,-27,-55,-26,-52,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-28,-29,-30,]),'EQ':([28,29,30,31,32,54,66,67,69,87,97,98,99,100,101,102,103,104,105,109,126,127,128,],[-5,-6,-7,-8,-9,94,-27,-55,-26,-52,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-28,-29,-30,]),')':([28,29,30,31,32,53,55,66,67,68,69,87,97,98,99,100,101,102,103,104,105,106,107,108,109,118,119,120,121,122,123,126,127,128,],[-5,-6,-7,-8,-9,88,95,-27,-55,105,-26,-52,-12,-13,-14,-15,-16,-17,-18,-19,-10,126,127,128,-49,-20,-21,-22,-23,-24,-25,-28,-29,-30,]),':':([28,29,30,31,32,66,67,69,87,96,97,98,99,100,101,102,103,104,105,109,126,127,128,],[-5,-6,-7,-8,-9,-27,-55,-26,-52,125,-12,-13,-14,-15,-16,-17,-18,-19,-10,-49,-28,-29,-30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions':([0,5,],[2,14,]),'instruction':([2,14,88,95,130,131,],[3,3,117,124,132,133,]),'array':([6,32,38,110,],[20,67,74,129,]),'expression':([12,13,15,16,17,18,19,21,22,23,33,34,47,48,49,50,51,56,58,59,60,61,62,63,64,65,70,71,72,76,89,90,91,92,93,94,125,],[27,40,42,43,44,45,46,40,54,54,68,69,82,83,84,85,86,96,97,98,99,100,101,102,103,104,106,107,108,111,118,119,120,121,122,123,131,]),'matrix':([12,13,15,16,17,18,19,21,22,23,33,34,47,48,49,50,51,56,58,59,60,61,62,63,64,65,70,71,72,76,89,90,91,92,93,94,125,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'list':([13,21,],[39,52,]),'condition':([22,23,],[53,55,]),'arraylist':([38,],[73,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions','program',1,'p_program','last_parser.py',30),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','last_parser.py',34),
  ('instructions -> <empty>','instructions',0,'p_instructions','last_parser.py',35),
  ('instruction -> ;','instruction',1,'p_empty_instruction','last_parser.py',39),
  ('expression -> INT','expression',1,'p_expression_value','last_parser.py',43),
  ('expression -> FLOAT','expression',1,'p_expression_value','last_parser.py',44),
  ('expression -> matrix','expression',1,'p_expression_value','last_parser.py',45),
  ('expression -> STRING','expression',1,'p_expression_value','last_parser.py',46),
  ('expression -> ID','expression',1,'p_expression_ID','last_parser.py',50),
  ('expression -> ( expression )','expression',3,'p_expression_gr','last_parser.py',54),
  ('instruction -> { instructions }','instruction',3,'p_instruction_scope','last_parser.py',58),
  ('expression -> expression + expression','expression',3,'p_expression_binop','last_parser.py',62),
  ('expression -> expression - expression','expression',3,'p_expression_binop','last_parser.py',63),
  ('expression -> expression * expression','expression',3,'p_expression_binop','last_parser.py',64),
  ('expression -> expression / expression','expression',3,'p_expression_binop','last_parser.py',65),
  ('expression -> expression M_ADD expression','expression',3,'p_expression_binop_matrix','last_parser.py',69),
  ('expression -> expression M_SUB expression','expression',3,'p_expression_binop_matrix','last_parser.py',70),
  ('expression -> expression M_MUL expression','expression',3,'p_expression_binop_matrix','last_parser.py',71),
  ('expression -> expression M_DIV expression','expression',3,'p_expression_binop_matrix','last_parser.py',72),
  ('condition -> expression < expression','condition',3,'p_expression_relation','last_parser.py',76),
  ('condition -> expression > expression','condition',3,'p_expression_relation','last_parser.py',77),
  ('condition -> expression LE expression','condition',3,'p_expression_relation','last_parser.py',78),
  ('condition -> expression GE expression','condition',3,'p_expression_relation','last_parser.py',79),
  ('condition -> expression NEQ expression','condition',3,'p_expression_relation','last_parser.py',80),
  ('condition -> expression EQ expression','condition',3,'p_expression_relation','last_parser.py',81),
  ('expression -> - expression','expression',2,'p_uminus','last_parser.py',85),
  ('matrix -> expression M_TRANSPOSE','matrix',2,'p_transpose','last_parser.py',89),
  ('matrix -> ZEROS ( expression )','matrix',4,'p_matrix_generator','last_parser.py',93),
  ('matrix -> ONES ( expression )','matrix',4,'p_matrix_generator','last_parser.py',94),
  ('matrix -> EYE ( expression )','matrix',4,'p_matrix_generator','last_parser.py',95),
  ('instruction -> ID = expression ;','instruction',4,'p_assignment','last_parser.py',99),
  ('instruction -> ID A_ADD expression ;','instruction',4,'p_assignment','last_parser.py',100),
  ('instruction -> ID A_SUB expression ;','instruction',4,'p_assignment','last_parser.py',101),
  ('instruction -> ID A_MUL expression ;','instruction',4,'p_assignment','last_parser.py',102),
  ('instruction -> ID A_DIV expression ;','instruction',4,'p_assignment','last_parser.py',103),
  ('instruction -> ID array = expression ;','instruction',5,'p_position_assignment','last_parser.py',107),
  ('instruction -> ID array A_ADD expression ;','instruction',5,'p_position_assignment','last_parser.py',108),
  ('instruction -> ID array A_SUB expression ;','instruction',5,'p_position_assignment','last_parser.py',109),
  ('instruction -> ID array A_MUL expression ;','instruction',5,'p_position_assignment','last_parser.py',110),
  ('instruction -> ID array A_DIV expression ;','instruction',5,'p_position_assignment','last_parser.py',111),
  ('instruction -> IF ( condition ) instruction','instruction',5,'p_if_else','last_parser.py',115),
  ('instruction -> IF ( condition ) instruction ELSE instruction','instruction',7,'p_if_else','last_parser.py',116),
  ('instruction -> WHILE ( condition ) instruction','instruction',5,'p_while','last_parser.py',120),
  ('instruction -> FOR ID = expression : expression instruction','instruction',7,'p_for','last_parser.py',124),
  ('instruction -> BREAK ;','instruction',2,'p_special_instruction','last_parser.py',128),
  ('instruction -> CONTINUE ;','instruction',2,'p_special_instruction','last_parser.py',129),
  ('instruction -> RETURN expression ;','instruction',3,'p_special_instruction','last_parser.py',130),
  ('instruction -> PRINT list ;','instruction',3,'p_print','last_parser.py',134),
  ('matrix -> [ arraylist ]','matrix',3,'p_matrix','last_parser.py',138),
  ('arraylist -> array','arraylist',1,'p_arraylist','last_parser.py',142),
  ('arraylist -> arraylist , array','arraylist',3,'p_arraylist','last_parser.py',143),
  ('array -> [ list ]','array',3,'p_array','last_parser.py',147),
  ('list -> expression','list',1,'p_list','last_parser.py',151),
  ('list -> list , expression','list',3,'p_list','last_parser.py',152),
  ('expression -> ID array','expression',2,'p_array_access','last_parser.py',156),
]
