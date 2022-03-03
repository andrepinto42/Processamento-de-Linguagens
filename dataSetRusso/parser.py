import re
import sys

parser = r'\d+ \d+ ((?:\w+ ){1,3})(\w{4} )(.+)'

oco = {}

for line in sys.stdin:
    m =re.search(parser,line)
    if (m):
        pal = m.groups()[2]
        if pal in oco:
            oco[pal] = oco[pal] + 1
        else:
            oco[pal] = 1
for k,v in oco.items():
    print(k,v)