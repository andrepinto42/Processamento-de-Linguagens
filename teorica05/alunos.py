import re
import sys

# aluno = r'\"?:<id>(\w+)\"()()()'

#Usar uma expressao regular com {3} causa com que o grupo nao seja caço
# aluno = r'(?:\"(.+)\",){3}(?:(\d+),){3}(\d+)'

aluno = r'(?:\"(?P<id>.+)\",)(?:\"(?P<nome>.+)\",)(?:\"(?P<curso>.+)\",)(?:(\d+),)(?:(\d+),)(?:(\d+),)(\d+)'

for linha in sys.stdin:
    m = re.search(aluno,linha)
    if (not m):
        print("No match bro")
        continue;

    dic = m.groupdict()
    print(dic)
    print(m.groups())