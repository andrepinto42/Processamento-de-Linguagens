
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "right=left+-left*/right^ID INT INTKEYWORD PRINTprog : decls instrsdecls : decls : decls decldecl : INTKEYWORD ID ';'instrs : instrs : instrs instr instr : ID '=' exp ';'instr : PRINT exp ';'exp : exp '+' expexp : exp '-' expexp : exp '*' expexp : exp '/' expexp : exp '^' expexp : INTexp : IDexp : '(' exp ')'exp : '.'"
    
_lr_action_items = {'INTKEYWORD':([0,2,4,16,],[-2,5,-3,-4,]),'ID':([0,2,3,4,5,6,8,10,14,16,18,19,20,21,22,23,25,],[-2,-5,7,-3,9,-6,13,13,13,-4,-8,13,13,13,13,13,-7,]),'PRINT':([0,2,3,4,6,16,18,25,],[-2,-5,8,-3,-6,-4,-8,-7,]),'$end':([0,1,2,3,4,6,16,18,25,],[-2,0,-5,-1,-3,-6,-4,-8,-7,]),'=':([7,],[10,]),'INT':([8,10,14,19,20,21,22,23,],[12,12,12,12,12,12,12,12,]),'(':([8,10,14,19,20,21,22,23,],[14,14,14,14,14,14,14,14,]),'.':([8,10,14,19,20,21,22,23,],[15,15,15,15,15,15,15,15,]),';':([9,11,12,13,15,17,26,27,28,29,30,31,],[16,18,-14,-15,-17,25,-9,-10,-11,-12,-13,-16,]),'+':([11,12,13,15,17,24,26,27,28,29,30,31,],[19,-14,-15,-17,19,19,-9,-10,-11,-12,-13,-16,]),'-':([11,12,13,15,17,24,26,27,28,29,30,31,],[20,-14,-15,-17,20,20,-9,-10,-11,-12,-13,-16,]),'*':([11,12,13,15,17,24,26,27,28,29,30,31,],[21,-14,-15,-17,21,21,21,21,-11,-12,-13,-16,]),'/':([11,12,13,15,17,24,26,27,28,29,30,31,],[22,-14,-15,-17,22,22,22,22,-11,-12,-13,-16,]),'^':([11,12,13,15,17,24,26,27,28,29,30,31,],[23,-14,-15,-17,23,23,23,23,23,23,23,-16,]),')':([12,13,15,24,26,27,28,29,30,31,],[-14,-15,-17,31,-9,-10,-11,-12,-13,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'decls':([0,],[2,]),'instrs':([2,],[3,]),'decl':([2,],[4,]),'instr':([3,],[6,]),'exp':([8,10,14,19,20,21,22,23,],[11,17,24,26,27,28,29,30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> decls instrs','prog',2,'p_prog','vms.py',49),
  ('decls -> <empty>','decls',0,'p_decls02','vms.py',51),
  ('decls -> decls decl','decls',2,'p_decls01','vms.py',52),
  ('decl -> INTKEYWORD ID ;','decl',3,'p_decl01','vms.py',54),
  ('instrs -> <empty>','instrs',0,'p_instrs01','vms.py',56),
  ('instrs -> instrs instr','instrs',2,'p_instrs02','vms.py',57),
  ('instr -> ID = exp ;','instr',4,'p_instr01','vms.py',59),
  ('instr -> PRINT exp ;','instr',3,'p_instr02','vms.py',60),
  ('exp -> exp + exp','exp',3,'p_exp_add','vms.py',64),
  ('exp -> exp - exp','exp',3,'p_exp_sub','vms.py',65),
  ('exp -> exp * exp','exp',3,'p_exp_mult','vms.py',66),
  ('exp -> exp / exp','exp',3,'p_exp_dividir','vms.py',67),
  ('exp -> exp ^ exp','exp',3,'p_exp_chapeu','vms.py',68),
  ('exp -> INT','exp',1,'p_exp_Int','vms.py',69),
  ('exp -> ID','exp',1,'p_exp_ID','vms.py',71),
  ('exp -> ( exp )','exp',3,'p_exp_parenteses','vms.py',72),
  ('exp -> .','exp',1,'p_exp_ponto','vms.py',73),
]
