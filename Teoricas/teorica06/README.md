# Apontamentos

* Há pelo menos uma verdadeira, ou pode bem haver mais.

* Assinalar uma falsa anula uma correta na pergunta.
* Perguntas nao tem cotaçao negativa

------------------
Expressão regular para um id

* id = r'[_A-Za-z]\w*

Expressão regular de um inteiro sem o sinal

* iss = \d+

Automato finito determinista 

AFD = (S, Z, Estados, funçãoTransição)

* Tem um estado final
* Conjunto de estados finais

* Tem uma função de transição


Automato finito não determinista

-------------

[Finite State Machine](https://madebyevan.com/fsm)

```
   d  _  letra
---------------
S  B  A  A
B  B  -  -
A  A  A  A
```
Maquina de estado do website

![](Screenshot%20from%202022-03-08%2009-31-10.png)

```python
inicial = S
final = B
estado = inicial

for t in input:
    estado = tabela[estado, t]

if (estado = final):
    print("Estamos numa situação de sucesso") 
```