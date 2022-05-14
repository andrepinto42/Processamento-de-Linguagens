import re
import sys

real_num = r'[+-]?\d+(?:\.\d+)?'

# Falta colocar as os paratenses para identificar o grupo correto 
coord = rf'\(({real_num}),\s*({real_num})\)'

for line in sys.stdin:
    line = re.sub(coord,r"<point lat='\1', lon='\2' />",line)
    if (line):
        print(line)    

quit()

# Tambem dá para executar assim

coord = rf'\((?P<lat>{real_num}),\s*(?P<lon>{real_num})\)'

for line in sys.stdin:
    line = re.sub(coord,r"<point lat='\g<lat>', lon='\g<lon>' />",line)
    if (line):
        print(line)