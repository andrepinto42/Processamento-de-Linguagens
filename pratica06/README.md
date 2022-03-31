# Gramatica

## Definir uma gramatica para reconhecer inteiros


```
NI -> Sinal NumeroInteiroSemSinal

NumeroInteiroSemSinal -> d
                       | d NumeroInteiroSemSinal
```

```
Sinal -> +
    |    -
    |   
```



```
d -> 1
    | 2
    | 3
    | 4
    | 5
    | 6
    | 7
    | 8
    | 9
    | 0
```

---------------

## Gramatica para definir uma lista de inteiros em Haskell
```haskell
[7,10,43]
```

`Simbolos Terminais = {0,1,2,3,4,5,6,7,8,9, [ , ] , , }`
```
Li -> '[' E ']'
Li -> '[' ']'

E  -> NI , E
E  | NI 
```

## Gramatica para definir uma lista de inteiros em Python

```python
[7,[],[9,[20,45]],15]
```

```
Li -> '[' E ']'
Li -> '[' ']'

E  -> N , E
E   | N

N  -> Li
    | NI
```

-------------------
### Representação da gramática da expressão

```python
[7,[],[9,[20,45]],15]
```


```
L1 => [E] => [N , ',' E] => [NI , ',' E] => [NI , ',' , N ',' E] 
```
Ainda falta completar...


----------------

Acabar processadorAUTOMATO.py

Verificar

[link da aula](natura.di.uminho.pt/~jj/pl-22)