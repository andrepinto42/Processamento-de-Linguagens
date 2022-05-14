import re
import sys

#Named Group

#Named group que apanha palavras e guarda no grupo que se chama pal

palavra = r'(?P<pal>\b\w+\b)'

for linha in sys.stdin:
    m = re.search(palavra,linha)
    if (not m):
        print("No match bro")
        continue;
    dic = m.groupdict()
    print(dic)
    # print("Group 1 = " + str(m.group(1)))
    print("Group pal = " + str(m.group('pal')))