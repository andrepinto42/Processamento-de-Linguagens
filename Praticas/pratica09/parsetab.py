
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "right=left+-left*/right^rightNEGATEDUMP ID INT NEGATE PRINTprog : comandoscomandos : comandos : comandos comando comando : ID '=' expcomando : expcomando : DUMPcomando : argsexp : exp '+' expexp : exp '-' expexp : exp '*' expexp : exp '/' expexp : exp '^' expexp : INTexp : IDexp : '(' exp ')'exp : '.'exp : NEGATE expexp : ID '=' expexp : ID '(' exp ')'exp : ID '(' exp ',' exp ')'args : expargs : args ',' expargs : exp ':' exp"
    
_lr_action_items = {'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,39,],[-2,4,-3,-14,-5,-6,-7,-13,22,-16,22,22,22,22,22,22,22,22,22,22,-14,-17,-4,-8,-9,-10,-11,-12,-23,-22,-15,22,-19,22,-18,-20,]),'DUMP':([0,2,3,4,5,6,7,8,10,22,23,24,26,27,28,29,30,31,32,33,35,37,39,],[-2,6,-3,-14,-5,-6,-7,-13,-16,-14,-17,-4,-8,-9,-10,-11,-12,-23,-22,-15,-19,-18,-20,]),'INT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,39,],[-2,8,-3,-14,-5,-6,-7,-13,8,-16,8,8,8,8,8,8,8,8,8,8,-14,-17,-4,-8,-9,-10,-11,-12,-23,-22,-15,8,-19,8,-18,-20,]),'(':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,39,],[-2,9,-3,13,-5,-6,-7,-13,9,-16,9,9,9,9,9,9,9,9,9,9,13,-17,-4,-8,-9,-10,-11,-12,-23,-22,-15,9,-19,9,-18,-20,]),'.':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,39,],[-2,10,-3,-14,-5,-6,-7,-13,10,-16,10,10,10,10,10,10,10,10,10,10,-14,-17,-4,-8,-9,-10,-11,-12,-23,-22,-15,10,-19,10,-18,-20,]),'NEGATE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,39,],[-2,11,-3,-14,-5,-6,-7,-13,11,-16,11,11,11,11,11,11,11,11,11,11,-14,-17,-4,-8,-9,-10,-11,-12,-23,-22,-15,11,-19,11,-18,-20,]),'$end':([0,1,2,3,4,5,6,7,8,10,22,23,24,26,27,28,29,30,31,32,33,35,37,39,],[-2,0,-1,-3,-14,-5,-6,-7,-13,-16,-14,-17,-4,-8,-9,-10,-11,-12,-23,-22,-15,-19,-18,-20,]),'=':([4,22,],[12,34,]),'+':([4,5,8,10,21,22,23,24,25,26,27,28,29,30,31,32,33,35,37,38,39,],[-14,14,-13,-16,14,-14,-17,14,14,-8,-9,-10,-11,-12,14,14,-15,-19,14,14,-20,]),'-':([4,5,8,10,21,22,23,24,25,26,27,28,29,30,31,32,33,35,37,38,39,],[-14,15,-13,-16,15,-14,-17,15,15,-8,-9,-10,-11,-12,15,15,-15,-19,15,15,-20,]),'*':([4,5,8,10,21,22,23,24,25,26,27,28,29,30,31,32,33,35,37,38,39,],[-14,16,-13,-16,16,-14,-17,16,16,16,16,-10,-11,-12,16,16,-15,-19,16,16,-20,]),'/':([4,5,8,10,21,22,23,24,25,26,27,28,29,30,31,32,33,35,37,38,39,],[-14,17,-13,-16,17,-14,-17,17,17,17,17,-10,-11,-12,17,17,-15,-19,17,17,-20,]),'^':([4,5,8,10,21,22,23,24,25,26,27,28,29,30,31,32,33,35,37,38,39,],[-14,18,-13,-16,18,-14,-17,18,18,18,18,18,18,18,18,18,-15,-19,18,18,-20,]),':':([4,5,8,10,22,23,24,26,27,28,29,30,33,35,37,39,],[-14,19,-13,-16,-14,-17,-18,-8,-9,-10,-11,-12,-15,-19,-18,-20,]),',':([4,5,7,8,10,22,23,24,25,26,27,28,29,30,31,32,33,35,37,39,],[-14,-21,20,-13,-16,-14,-17,-18,36,-8,-9,-10,-11,-12,-23,-22,-15,-19,-18,-20,]),')':([8,10,21,22,23,25,26,27,28,29,30,33,35,37,38,39,],[-13,-16,33,-14,-17,35,-8,-9,-10,-11,-12,-15,-19,-18,39,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'comandos':([0,],[2,]),'comando':([2,],[3,]),'exp':([2,9,11,12,13,14,15,16,17,18,19,20,34,36,],[5,21,23,24,25,26,27,28,29,30,31,32,37,38,]),'args':([2,],[7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> comandos','prog',1,'p_prog','operadoresUnarios.py',55),
  ('comandos -> <empty>','comandos',0,'p_comandos_varios01','operadoresUnarios.py',56),
  ('comandos -> comandos comando','comandos',2,'p_comandos_varios02','operadoresUnarios.py',57),
  ('comando -> ID = exp','comando',3,'p_comando01','operadoresUnarios.py',59),
  ('comando -> exp','comando',1,'p_comando02','operadoresUnarios.py',61),
  ('comando -> DUMP','comando',1,'p_comando04','operadoresUnarios.py',62),
  ('comando -> args','comando',1,'p_comando05','operadoresUnarios.py',63),
  ('exp -> exp + exp','exp',3,'p_exp_add','operadoresUnarios.py',66),
  ('exp -> exp - exp','exp',3,'p_exp_sub','operadoresUnarios.py',67),
  ('exp -> exp * exp','exp',3,'p_exp_mult','operadoresUnarios.py',68),
  ('exp -> exp / exp','exp',3,'p_exp_dividir','operadoresUnarios.py',69),
  ('exp -> exp ^ exp','exp',3,'p_exp_chapeu','operadoresUnarios.py',70),
  ('exp -> INT','exp',1,'p_exp_Int','operadoresUnarios.py',71),
  ('exp -> ID','exp',1,'p_exp_ID','operadoresUnarios.py',73),
  ('exp -> ( exp )','exp',3,'p_exp_parenteses','operadoresUnarios.py',74),
  ('exp -> .','exp',1,'p_exp_ponto','operadoresUnarios.py',75),
  ('exp -> NEGATE exp','exp',2,'p_exp_Negate','operadoresUnarios.py',76),
  ('exp -> ID = exp','exp',3,'p_exp_comboio','operadoresUnarios.py',79),
  ('exp -> ID ( exp )','exp',4,'p_exp_ExpressaoMatematica','operadoresUnarios.py',82),
  ('exp -> ID ( exp , exp )','exp',6,'p_exp_ExpressaoMatematica2','operadoresUnarios.py',87),
  ('args -> exp','args',1,'p_args2','operadoresUnarios.py',92),
  ('args -> args , exp','args',3,'p_args3','operadoresUnarios.py',96),
  ('args -> exp : exp','args',3,'p_args4','operadoresUnarios.py',101),
]
