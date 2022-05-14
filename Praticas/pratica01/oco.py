#!/usr/bin/env python3
import sys

txt = sys.stdin.read()

oco = {}

for pal in txt.split():
    if pal in oco:
        oco[pal] = oco[pal] + 1
    else:
        oco[pal] = 1
for k,v in oco.items():
    print(v,"\t",k)

