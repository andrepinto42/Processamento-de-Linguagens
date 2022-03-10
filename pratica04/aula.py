import sys
import re

# Estrutura do poema
t = '''title:t
author:a

a
b
c
d

e
f
g
'''

f = open("musica2022/musica/gal-chuvaDePrata.lyr",'r')
music = f.read()

cabecalho,poema = re.split(r'\n\n+',music,maxsplit=1)

cabecalho = re.sub(r'title:\s*(.+)',r'<h1>\1</h1>',cabecalho)
cabecalho = re.sub(r'(.+):\s*(.+)',r'<h2>\1:\2</h2>',cabecalho)

print(f'''
<body>
    <hr/>
        {cabecalho}
    <hr/>
    <pre>
        {poema}
    </pre>
</body>
''')