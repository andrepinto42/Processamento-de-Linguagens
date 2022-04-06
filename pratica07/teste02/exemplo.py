import re

texto ='''
===t1
<h1>{{v1}}</h1>


{{L1,T2}}



===T2

viva o Salgueiros
'''

def compilaTemplates(txt):
    texto_Separado = re.split(r'===',texto)

    #Deitar fora o primeiro bocado do split pois e inutil
    texto_Separado.pop(0)
    for t in texto_Separado:
        t = re.sub(r'(\w+)(.+)',r"def \1(d): return '''\2''' ",t,flags=re.S)
        #Executar as funcoes
        exec(t,globals())




compilaTemplates(texto)

print(t1(7))