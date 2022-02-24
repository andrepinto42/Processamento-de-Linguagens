# Prática

## Inicialização

Fazer download do [Material](https://nature.di.uminho.pt/~jj/pl-22)

Estando na diretoria do source

```
cat musica2022/musica/* > grande.txt
```
Colocar toda a informação disponivel das músicas em um só ficheiro

-----

Contem 989 musicas que vamos usar para fazer parsing do seu conteudo
* Descobrir *autor*, *ano*, *titulo*
* Descobrir *lyrics*
* Descobrir a *pauta* musical de uma música

-------

### Comandos
comando `grep` conhece expressoes regulares

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
Usar *regular expressions* dentro do editor de texto

Expressão a procurar :
* `title: *(.*)`

Procura todas as strings que comecam por `title:` e apanha tudo que tiver à frente e ***agrupa o que apanhou para o grupo 1***

replace:
* `<h1>$1</h1>` 


--------------

## Comandos da *bash* para gerar ficheiros HTML

```
 perl -pe 's!title: *(.*)!<h1>$1</h1>!' grande.txt > _2.html
```

Gera um ficheiro HTML onde substitui title: "titulo" por uma *tag* HTML

```
title: António variações    | original
<h1>António variações</h1>  | final
```

De seguida abrir o ficheiro HTML
```
firefox _2.html
```  



 ------------

 perl -p

> Substitui a linha e depois dá print denovo

 ---------

regex(a)

string : aaaaaaaaaaaaaaa

substitute : ($1)

result -> (a)(a)(a)(a)(a)(a)(a)(a)(a)(a)(a)(a)(a)(a)(a)

 -------------------

### **SED**

 sed -> stream editor

_COMANDOS PARA EXECUTAR_

* sed -rn '/title:/ s!title!!;p' grande.txt 

* sed -rn '/title:/ s!title:!!p' grande.txt 

* sed -rn '/author:/ s!author: !!p' grande.txt | sed -r 's!\s*;\s*!\n!g'

* sed -rn '/author:/ s!author: !!p' grande.txt | sed -r 's!\s*;\s*!\n!g' | sort | uniq -c | sort -n


-------------

grep -P
>expressoes regulares do Pearl

grep -z

>expressoes regulares linha  a linha 

### SED
```
sed -rn '/<abc/,/<.abc>/p' grande.txt
```
### grep
```
grep -P -zo '<abc>(.*\n)*?</abc>' grande.txt
```
comando demasiado *complexo*
```
grep -P -zo '<abc>[^<]*</abc>' grande.txt
```
Mesmo comando mas mais *simples*

Redirecionar para o ficheiro x.abc
```
grep -P -zo '<abc>[^<]*</abc>' grande.txt > x.abc
```
----------------

executar:

>abcm2ps x.abc

Isto cria o ficheiro *Out.ps* que contém uma pauta de musica :)

-----------


# TPC

* procurar acordes de viola

* eles tao em linha em que se encontram dois ou mais espacos

* Fazer mais exercicios de extracao ou de procura?

* Trazer para a aula 2 exercicios

* Extrair algo que nos inventamos