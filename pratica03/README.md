---
title : Diario de Bordo
author: Pinto
---

# Apontamentos

*Site da aula passada*

https://natura.di.uminho.pt/~jj/pl-22/02-24

Gera um pdf
```
pandoc README.md -o _.pdf
```

Gera um pdf com slides
```
pandoc README.md -t beamer -o _.pdf
```

open files
```
xdg-open _.pdf
```
--------------------

Funções de expressoes regulares
```
search(re,str,...)
findall(re,str,...)
sub(re,...,str,...)
split(re,str,...)
```


------

string = r'' -> retira o sentido da string

string = f'' -> ?

---------

flag = re.I -> *Ignora o case*

-----------
 ## History

70  python3 test.py 
71  cd pratica03
72  python3 test.py 
73  touch test.txt
74  code test.
75  code test.txt
76  python3 test.py
77  code latitude_longitude.py
78  touch lat_long_Test.txt
79  code lat_long_Test.txt 
80  python3 latitude_longitude.py 
81  cat lat_long_Test.txt | python3 latitude_longitude.py 
82  od -c
83  cat lat_long_Test.txt | python3 latitude_longitude.py | od -c
84  cat lat_long_Test.txt | python3 latitude_longitude.py 
85  python3 latitude_longitude.py 
86  cat lat_long_Test.txt | python3 latitude_longitude.py 
87  cp latitude_longitude.py finalAula.py
88  code finalAula.py 
89  cat lat_long_Test.txt | python3 finalAula.py 
90  history