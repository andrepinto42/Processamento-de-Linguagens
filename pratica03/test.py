import re

str1 ="Esta ´e uma linha de lixo."
str2 = "121.18.19.20"
str3 = "2001:0db8:0000:0000:0000:ff00:0042:8329"
str4 = "epl.di.uminho.pt 193.136.19.129"

# Errado
# matchIPV4 = r'(\d+).(\d+).(\d+).(\d+)'
# matchIPV4 = r'.*'

# Apanha um numero entre 0 e 255 que tenha 3 carateres no maxima
#Algo esta errado
# ele4 =  r'2(5[0-5]|[0-4]\d)|[0-1]\d\d|\d\d|\d'

ele4 = r'(\d+){1,3}'
matchIPV4 = fr'({ele4}\.){{3}}{ele4}'

ele6 = r'([0-9a-f]{4})'
#Algo esta errado
matchIPV6 = fr'([0-9a-f]{4}:){7}([0-9a-f]{4})'
matchIPV6 = fr'({ele6}:){{7}}({ele6}{{4}})'

def testa4(line):
    for unit in re.split(r'\.',line):
        if not (0 <= int(unit) <= 255) :
            return False
    return True


with open("test.txt") as file:
    lines = file.readlines()

for line in lines: 
    #Comer os espacos no inicio e no fim
    line = line.strip();

    if re.search(matchIPV6,line):
        print(f"Matched IPV6 {line}");
    elif re.search(matchIPV4,line):
        if testa4(line):
            print(f"Matched IVP4 {line}");
        else:
            print("Match Invalido de IPV4",line)
    else: 
        print("NO match");