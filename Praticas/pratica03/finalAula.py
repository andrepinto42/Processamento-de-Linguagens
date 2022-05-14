import re
import sys

def add_coords(matcher):
    return f"<somadas {float(matcher[1]) + float(matcher[2])} >"

real_num = r'[+-]?\d+(?:\.\d+)?'

coord = rf'\(({real_num}),\s*({real_num})\)'

for line in sys.stdin:
    line = re.sub(coord,add_coords,line)
    if (line):
        print(line)