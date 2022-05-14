import re
import sys

### Gerar expressao regular
p = re.compile(r'\d+')

### Ler da consola o que dá match com a nossa expressao
linha = sys.stdin;
print(p.match(str(linha)))