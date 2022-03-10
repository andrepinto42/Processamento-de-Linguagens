import sys
import re

# Correr com
# python3 aula02.py musica2022/musica/*.lyr
# cat index.html
# xdg-open index.html

def handleTudo(nomeFile):
    f = open(nomeFile,'r')
    index = open("index.html",'a')
    saida = re.sub(r'(.+)\.lyr$',r'\1.html',nomeFile)
    out = open(saida,'w')
    music = f.read()

    cabecalho,poema = re.split(r'\n\n',music,maxsplit=1)
    # Tratar do titulo
    cabecalho = re.sub(r'title:\s*(.+)',r'<h1>\1</h1>',cabecalho)
    # Tratar do resto da informacao
    cabecalho = re.sub(r'(.+):\s*(.+)',r'<h2>\1:\2</h2>',cabecalho)
    
    match_title =re.search(r'<h1>(.+)</h1>',cabecalho)
    if match_title is not None:
        # Falta qualquer coisa aqui
        print(f'''<li><a href="{saida}">{match_title[1]}</a><a></li>''',file=index)
    
    print(f'''
    <body>
        <hr/>
{cabecalho}
        <hr/>
        <pre>
{poema}
        </pre>
    </body>
    ''',file=out)
    out.close()
    f.close()
    index.close();

    


index = open("index.html",'w')
print(r'<h1>Indice geral das musicas</h1>',file=index)
index.close()

for execs in sys.argv[1:]:# python3 aula02.py ola
    handleTudo(execs)