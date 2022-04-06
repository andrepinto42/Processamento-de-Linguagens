#String para reconhecer diretorias e ficheiros
'''
PL{DOC{TP},AULAS{03-13{DB{},x.py}}}
'''

'''
FS -> Dir

Dir -> id '{' Filhos '}'
Dir -> id '{' '}'
Filhos -> Filho
        | Filho ',' Filhos

Filho -> id
Filho -> dir
'''