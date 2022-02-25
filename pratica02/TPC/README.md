# TPC

Ficheiro que contem um dataset de transferencias pokemon

_wonder trade.csv_

```
Date,Time,Pokemon,Trainer Region,Trainer Subregion,Pokemon Region,Level,Level Met,Gender,Type1,Type2,Nature,Pokeball,Held Item,Perfect IVs
12/13/16,17:28,Oricorio,South Korea,,,13,10,F,Electric,Flying,Sassy,Poke,F,0
12/13/16,17:30,Zubat,United States,Texas,GER,8,8,M,Poison,Flying,Hardy,Poke,F,1
12/13/16,17:31,Carbink,United States,Oklahoma,,10,10,N,Rock,Fairy,Relaxed,Poke,F,0
12/13/16,17:33,Klefki,United States,Connecticut,,29,29,M,Steel,Fairy,Jolly,Quick,F,0
12/13/16,17:34,Luvdisc,United States,,,16,16,M,Water,,Naughty,Quick,F,0
```

Buscar qual o *pokemon* que é transferido

Expressões tentadas

```
([0-9]{2}\/){2}[0-9]{2},.*,
```
***Resultado***

```
12/13/16,17:28,Oricorio,South Korea,,,13,10,F,Electric,Flying,Sassy,Poke,F,
```

Esta expressao nao funciona pois o (.*,) vai procurar a linha até ao fim, depois percorre do fim até ao inicio para encontrar um ","

-------

Melhoria -> Adicionar o operador "?" para não fazer uma pesquisa greedy

_Dessa forma vai fazer match se encontrar com o primeiro ','_

```
([0-9]{2}\/){2}[0-9]{2},.*?,
```
***Resultado***
```
12/13/16,17:30,
```

--------
Melhoria -> Agrupar as expressoes de captura para ser mais facil de substituir
```
(.*?),(.*?),(.*?),.*
```

![](docPokemonRegex.PNG)

Agora é só necessário substituir o grupo que achamos relevante pelo o que queremos


----------------

# Notas Finais de Algoritmos 2020

Estrutura da documentação
```
93173 André Gonçalves Pinto MIEI 11.0 10.5 F 11
```
Nota Final está representada como a ultima entrada
![](docAlgoritmos.PNG)

Regex: `(F|R|(TG))$`

> Resultados encontrados -> ***323 matches***

Numero de alunos inscritos -> ***524***

Taxa de reprovação **total** de `61,6%`

## Alunos de MIEI

```
(MIEI).*(F|R|(TG))$
```
> Resultados encontrados -> ***212 matches***

> Alunos totais -> ***372***

Taxa de reprovação de `56,9%`

--------

## Alunos de LCC

```
(LCC).*(F|R|(TG))$
```
> Resultados encontrados -> ***108 matches***

> Alunos totais -> ***145***

Taxa de reprovação de `74,5%`

-------------

## Época Especial

Alunos inscritos -> ***60***

Alunos reprovados -> **53**

Taxa de reprovação de `88,3%`
