# Apontamentos

Entregas de trabalho 
* 25 março TP1 
* 9 Maio TP2

-------------

Expressoes Regulares - Linguagens Regulares

*É necessário algo mais que expressoes regulares para compilar uma linguagem*

Para isso existem as *Autómatos Finitos Deterministas*

--------------
Também existe
## Gramáticas Regulares

### Regras para a construcao de frases

T -> Conjunto de palavras, tokens

N -> Simbolos

S -> Símbolo nao terminal especial, ponto inicial da gramatica

P -> Conjunto P de regras, mediante as restriçoes que são colocados neste grupo temos um certo tipo de linguagem


Simbolos Terminais:
1. Sinais: são constituidos por um caráter
2. Palavras reservadas:  string constantes
3. Terminais variáveis: identificadores, inteiros, etc; *Definidos por expressões regulares*


Exemplo de frases validas
* ()
* (())
* ((())())
```
T = { ')', '(' }
N = { }
P = {S -> ... }
```

Outro *exemplo*

Exemplo de frases validas
* [ ]
* [1]
* [1,2,3]

```
T = { '[', ']', inteiro, ','}
N = {S, Conteúdo, Cont}
P = {
        S -> '[' Conteúdo  ']'
        Conteúdo -> inteiro Cont
                    | vazio 
        Conteúdo -> vazio
        Cont -> vazio
                | ',' inteiro Cont // falha neste condição

    }
// Na gramática regular não pode ter mais do lado esquerdo 1 terminal e 1 regular
```

---------------------
## Maquina de Estado para um inteiro
Representação de um inteiro REGEX:

`inteiro = (\+|-)?\d+`


|Estado|+|-|d|
|:-:|-|-|-|
S|A|A|B
A|-|-|B
B|-|-|B

Conversão para máquina de estado
```
S -> '+' A

    |'-' A

    | D  B

A -> d  

B -> d  B
    | E
```
---------------

## Automato Finito

Q - Conjunto de Estados

E - alfabeto

q0 - estado inicial

A c Q - Conjunto estados finitos/ aceitação

d . Q * E -> Q
 