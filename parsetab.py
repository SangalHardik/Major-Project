_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CIN COUT DECREMENT DOUBLE_EQUALS ELSE ELSEIF EQUALS FOR GREATER ID IDENTIFIER IF INCREMENT LCURLY LEFTSHIFT LESS LPAR MINUS MINUSEQUAL OPERATOR PLUS PLUSEQUAL RCURLY RIGHTSHIFT RPAR SEMICOLON STRING THEN WHILE\n    statement : s1 s2\n            | empty\n    \n    s1 : var_declaration_statement\n          | if_expression\n          | io_statement\n          | loop_expression\n          | STRING SEMICOLON\n          | empty\n    \n    s2 : statement\n    \n    io_statement : CIN RIGHTSHIFT STRING SEMICOLON\n                 | COUT LEFTSHIFT STRING SEMICOLON\n    \n    var_declaration_statement : IDENTIFIER STRING SEMICOLON\n    \n    loop_expression : WHILE condition LCURLY statement RCURLY\n                    | FOR forcondition LCURLY statement RCURLY\n    \n    condition : LPAR expression RPAR\n    \n    forcondition : LPAR expression SEMICOLON expression SEMICOLON expression RPAR\n                | LPAR IDENTIFIER expression SEMICOLON expression SEMICOLON expression RPAR\n    \n    if_expression : IF condition LCURLY statement RCURLY else_expression\n                | IF condition LCURLY statement RCURLY elseif_expression\n    \n    elseif_expression : ELSE IF condition LCURLY statement RCURLY elseif_expression\n                        | ELSE IF condition LCURLY statement RCURLY else_expression\n                      | empty\n    \n    else_expression : ELSE LCURLY statement RCURLY\n                    | empty\n    \n    expression : STRING\n               | ID\n               | empty\n\n    empty : '
    
_lr_action_items = {'STRING':([0,2,3,4,5,6,7,9,17,20,21,22,25,26,27,34,35,37,40,41,44,46,47,48,50,51,52,54,55,57,60,65,66,69,71,72,73,],[8,8,-8,-3,-4,-5,-6,18,-7,29,32,33,29,-12,8,8,8,29,-10,-11,29,-28,-13,-14,29,-18,-19,-22,29,8,29,-23,8,-28,-20,-21,-22,]),'$end':([0,1,2,3,4,5,6,7,15,16,17,26,40,41,46,47,48,51,52,54,65,69,71,72,73,],[-28,0,-28,-2,-3,-4,-5,-6,-1,-9,-7,-12,-10,-11,-28,-13,-14,-18,-19,-22,-23,-28,-20,-21,-22,]),'IDENTIFIER':([0,2,3,4,5,6,7,17,25,26,27,34,35,40,41,46,47,48,51,52,54,57,65,66,69,71,72,73,],[9,9,-8,-3,-4,-5,-6,-7,37,-12,9,9,9,-10,-11,-28,-13,-14,-18,-19,-22,9,-23,9,-28,-20,-21,-22,]),'IF':([0,2,3,4,5,6,7,17,26,27,34,35,40,41,46,47,48,51,52,53,54,57,65,66,69,70,71,72,73,],[10,10,-8,-3,-4,-5,-6,-7,-12,10,10,10,-10,-11,-28,-13,-14,-18,-19,58,-22,10,-23,10,-28,58,-20,-21,-22,]),'CIN':([0,2,3,4,5,6,7,17,26,27,34,35,40,41,46,47,48,51,52,54,57,65,66,69,71,72,73,],[11,11,-8,-3,-4,-5,-6,-7,-12,11,11,11,-10,-11,-28,-13,-14,-18,-19,-22,11,-23,11,-28,-20,-21,-22,]),'COUT':([0,2,3,4,5,6,7,17,26,27,34,35,40,41,46,47,48,51,52,54,57,65,66,69,71,72,73,],[12,12,-8,-3,-4,-5,-6,-7,-12,12,12,12,-10,-11,-28,-13,-14,-18,-19,-22,12,-23,12,-28,-20,-21,-22,]),'WHILE':([0,2,3,4,5,6,7,17,26,27,34,35,40,41,46,47,48,51,52,54,57,65,66,69,71,72,73,],[13,13,-8,-3,-4,-5,-6,-7,-12,13,13,13,-10,-11,-28,-13,-14,-18,-19,-22,13,-23,13,-28,-20,-21,-22,]),'FOR':([0,2,3,4,5,6,7,17,26,27,34,35,40,41,46,47,48,51,52,54,57,65,66,69,71,72,73,],[14,14,-8,-3,-4,-5,-6,-7,-12,14,14,14,-10,-11,-28,-13,-14,-18,-19,-22,14,-23,14,-28,-20,-21,-22,]),'RCURLY':([2,3,4,5,6,7,15,16,17,26,27,34,35,38,40,41,42,43,46,47,48,51,52,54,57,61,65,66,68,69,71,72,73,],[-28,-2,-3,-4,-5,-6,-1,-9,-7,-12,-28,-28,-28,46,-10,-11,47,48,-28,-13,-14,-18,-19,-22,-28,65,-23,-28,69,-28,-20,-21,-22,]),'SEMICOLON':([8,18,25,29,30,31,32,33,36,37,44,45,49,50,56,],[17,26,-28,-25,-26,-27,40,41,44,-28,-28,50,55,-28,60,]),'LPAR':([10,13,14,58,],[20,20,25,20,]),'RIGHTSHIFT':([11,],[21,]),'LEFTSHIFT':([12,],[22,]),'LCURLY':([19,23,24,39,53,62,63,67,70,],[27,34,35,-15,57,66,-16,-17,57,]),'ID':([20,25,37,44,50,55,60,],[30,30,30,30,30,30,30,]),'RPAR':([20,28,29,30,31,55,59,60,64,],[-28,39,-25,-26,-27,-28,63,-28,67,]),'ELSE':([46,69,],[53,70,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,2,27,34,35,57,66,],[1,16,38,42,43,61,68,]),'s1':([0,2,27,34,35,57,66,],[2,2,2,2,2,2,2,]),'empty':([0,2,20,25,27,34,35,37,44,46,50,55,57,60,66,69,],[3,3,31,31,3,3,3,31,31,54,31,31,3,31,3,73,]),'var_declaration_statement':([0,2,27,34,35,57,66,],[4,4,4,4,4,4,4,]),'if_expression':([0,2,27,34,35,57,66,],[5,5,5,5,5,5,5,]),'io_statement':([0,2,27,34,35,57,66,],[6,6,6,6,6,6,6,]),'loop_expression':([0,2,27,34,35,57,66,],[7,7,7,7,7,7,7,]),'s2':([2,],[15,]),'condition':([10,13,58,],[19,23,62,]),'forcondition':([14,],[24,]),'expression':([20,25,37,44,50,55,60,],[28,36,45,49,56,59,64,]),'else_expression':([46,69,],[51,72,]),'elseif_expression':([46,69,],[52,71,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> s1 s2','statement',2,'p_statement','plyparser.py',18),
  ('statement -> empty','statement',1,'p_statement','plyparser.py',19),
  ('s1 -> var_declaration_statement','s1',1,'p_s1','plyparser.py',36),
  ('s1 -> if_expression','s1',1,'p_s1','plyparser.py',37),
  ('s1 -> io_statement','s1',1,'p_s1','plyparser.py',38),
  ('s1 -> loop_expression','s1',1,'p_s1','plyparser.py',39),
  ('s1 -> STRING SEMICOLON','s1',2,'p_s1','plyparser.py',40),
  ('s1 -> empty','s1',1,'p_s1','plyparser.py',41),
  ('s2 -> statement','s2',1,'p_s2','plyparser.py',51),
  ('io_statement -> CIN RIGHTSHIFT STRING SEMICOLON','io_statement',4,'p_io_statement','plyparser.py',61),
  ('io_statement -> COUT LEFTSHIFT STRING SEMICOLON','io_statement',4,'p_io_statement','plyparser.py',62),
  ('var_declaration_statement -> IDENTIFIER STRING SEMICOLON','var_declaration_statement',3,'p_var_declaration_statement','plyparser.py',73),
  ('loop_expression -> WHILE condition LCURLY statement RCURLY','loop_expression',5,'p_loop_expression','plyparser.py',84),
  ('loop_expression -> FOR forcondition LCURLY statement RCURLY','loop_expression',5,'p_loop_expression','plyparser.py',85),
  ('condition -> LPAR expression RPAR','condition',3,'p_condition','plyparser.py',96),
  ('forcondition -> LPAR expression SEMICOLON expression SEMICOLON expression RPAR','forcondition',7,'p_forcondition','plyparser.py',106),
  ('forcondition -> LPAR IDENTIFIER expression SEMICOLON expression SEMICOLON expression RPAR','forcondition',8,'p_forcondition','plyparser.py',107),
  ('if_expression -> IF condition LCURLY statement RCURLY else_expression','if_expression',6,'p_if_expression','plyparser.py',122),
  ('if_expression -> IF condition LCURLY statement RCURLY elseif_expression','if_expression',6,'p_if_expression','plyparser.py',123),
  ('elseif_expression -> ELSE IF condition LCURLY statement RCURLY elseif_expression','elseif_expression',7,'p_elseif_expression','plyparser.py',139),
  ('elseif_expression -> ELSE IF condition LCURLY statement RCURLY else_expression','elseif_expression',7,'p_elseif_expression','plyparser.py',140),
  ('elseif_expression -> empty','elseif_expression',1,'p_elseif_expression','plyparser.py',141),
  ('else_expression -> ELSE LCURLY statement RCURLY','else_expression',4,'p_else_expression','plyparser.py',162),
  ('else_expression -> empty','else_expression',1,'p_else_expression','plyparser.py',163),
  ('expression -> STRING','expression',1,'p_expression_string_id','plyparser.py',180),
  ('expression -> ID','expression',1,'p_expression_string_id','plyparser.py',181),
  ('expression -> empty','expression',1,'p_expression_string_id','plyparser.py',182),
  ('empty -> <empty>','empty',0,'p_empty','plyparser.py',193),
]