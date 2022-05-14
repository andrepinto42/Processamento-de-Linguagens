
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "DUMP ID INT PRINT READprog : comandoscomandos : comandos : comandos comandocomando : atribcomando : printcomando : readcomando : dumpatrib : ID '=' Expprint : PRINT Expread : READ IDdump : DUMPExp : Exp '+' ExpExp : Exp '-' ExpExp : INTExp : ID"
    
_lr_action_items = {'ID':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,],[-2,8,-3,-4,-5,-6,-7,15,16,-11,15,-9,-14,-15,-10,-8,15,15,-12,-13,]),'PRINT':([0,2,3,4,5,6,7,11,13,14,15,16,17,20,21,],[-2,9,-3,-4,-5,-6,-7,-11,-9,-14,-15,-10,-8,-12,-13,]),'READ':([0,2,3,4,5,6,7,11,13,14,15,16,17,20,21,],[-2,10,-3,-4,-5,-6,-7,-11,-9,-14,-15,-10,-8,-12,-13,]),'DUMP':([0,2,3,4,5,6,7,11,13,14,15,16,17,20,21,],[-2,11,-3,-4,-5,-6,-7,-11,-9,-14,-15,-10,-8,-12,-13,]),'$end':([0,1,2,3,4,5,6,7,11,13,14,15,16,17,20,21,],[-2,0,-1,-3,-4,-5,-6,-7,-11,-9,-14,-15,-10,-8,-12,-13,]),'=':([8,],[12,]),'INT':([9,12,18,19,],[14,14,14,14,]),'+':([13,14,15,17,20,21,],[18,-14,-15,18,18,18,]),'-':([13,14,15,17,20,21,],[19,-14,-15,19,19,19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'comandos':([0,],[2,]),'comando':([2,],[3,]),'atrib':([2,],[4,]),'print':([2,],[5,]),'read':([2,],[6,]),'dump':([2,],[7,]),'Exp':([9,12,18,19,],[13,17,20,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> comandos','prog',1,'p_prog','yacc.py',6),
  ('comandos -> <empty>','comandos',0,'p_comandos_varios01','yacc.py',9),
  ('comandos -> comandos comando','comandos',2,'p_comandos_varios02','yacc.py',12),
  ('comando -> atrib','comando',1,'p_comando01','yacc.py',15),
  ('comando -> print','comando',1,'p_comando02','yacc.py',19),
  ('comando -> read','comando',1,'p_comando03','yacc.py',22),
  ('comando -> dump','comando',1,'p_comando04','yacc.py',25),
  ('atrib -> ID = Exp','atrib',3,'p_atrib','yacc.py',29),
  ('print -> PRINT Exp','print',2,'p_print','yacc.py',34),
  ('read -> READ ID','read',2,'p_read','yacc.py',37),
  ('dump -> DUMP','dump',1,'p_dump','yacc.py',40),
  ('Exp -> Exp + Exp','Exp',3,'p_Exp01','yacc.py',43),
  ('Exp -> Exp - Exp','Exp',3,'p_Exp02','yacc.py',46),
  ('Exp -> INT','Exp',1,'p_Exp03','yacc.py',49),
  ('Exp -> ID','Exp',1,'p_Exp04','yacc.py',52),
]