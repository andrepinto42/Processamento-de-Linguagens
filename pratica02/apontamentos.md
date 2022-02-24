# Prática

*Maquina nativa do stor?*

https://nature.di.uminho.pt/~jj/pl-22

Directory : musica2022/

Contem 989 musicas

-------

### Comandos
_**comando grep conhece expressoes regulares**_

usar o . para dar match com qualquer carater

grep 'Antonio' grande.txt

grep 'title.*Deolinda' grande.txt

grep -o 'title.*Deolinda' grande.txt -> mostra a linha toda

[0-9]{4} buscar uma data de um ano


^[^:]*[0-9]{4}
> ^ apanha a linha toda ^--------------

> $ apanha a linha toda ---------$

> apanha o primeiro carater que nao seja o ^ até o chegar ao carater que é um ^
--------------------
regular Expression :

title: \*(.\*)

replace:

\<h1>$1</h1\>


--------------


 2026  perl -pe 's!title: \*(.\*)!\<h1>$1</h1\>!' grande.txt > _2.html

 
 2027  firefox _2.html 
 
 2028  cp grande.txt _1.html
 
 2029  firefox _1.html 
 
 2030  cp grande.txt _1.html
 
 2031  firefox _1.html 
 
 2032  history


 ------------

 perl -p

 substitui a linha e depois dá print denovo



 ---------

 regex(a)

 string : aaaaaaaaaaaaaaa

 substitute : ($1)

 result -> (a)(a)(a)(a)(a)(a)(a)(a)(a)(a)(a)(a)(a)(a)(a)

 -------------------

### SED

 sed -> stream editor

_COMANDOS** PARA EXECUTAR_

* sed -rn '/title:/ s!title!!;p' grande.txt 

* sed -rn '/title:/ s!title:!!p' grande.txt 

* sed -rn '/author:/ s!author: !!p' grande.txt | sed -r 's!\s*;\s*!\n!g'

* sed -rn '/author:/ s!author: !!p' grande.txt | sed -r 's!\s*;\s*!\n!g' | sort | uniq -c | sort -n


-------------

grep -P

expressoes regulares do Pearl
grep -z

expressoes regulares linha  a linha 

### SED

sed -rn '/<abc/,/<.abc>/p' grande.txt

### grep
grep -P -zo '<abc>(.*\n)*?</abc>' grande.txt // comando demasiado complexo

grep -P -zo '<abc>[^<]*</abc>' grande.txt  // mesmo comando mas mais simples

----------------

executar:

>abcm2ps x.abc

Out.ps contem uma pauta de musica

-----------


# TPC

* procurar acordes de viola

* eles tao em linha em que se encontram dois ou mais espacos

* Fazer mais exercicios de extracao ou de procura?

* Trazer para a aula 2 exercicios

* Extrair algo que nos inventamos