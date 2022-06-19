import os
os.system('clang-format -style=Google -i ./out7.c')


with open('out7.c', 'r') as f:
    Lines = f.readlines()


for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()


dataTypes = ["char", "float", "double", "int",
             "long", "long int", "long long", "long long int"]

chk = 0
for i in range(len(Lines)):
    if("int main" in Lines[i]):
        chk = 1
        continue
    if(chk != 1):
        continue
    if("for" in Lines[i]):
        continue
    if("malloc" in Lines[i]):
        continue
    if("*" in Lines[i]):
        continue
    if("=" in Lines[i]):
        continue
    if("scanf" in Lines[i]):
        tempStr = ""
        tempStr = tempStr + \
            "if(1) { " + Lines[i] + "} else { printf(\"Error\");}"
        Lines[i] = tempStr
        continue
    if("printf" in Lines[i]):
        tempStr = ""
        tempStr = tempStr + \
            "if(1) { " + Lines[i] + "} else { printf(\"Error\");}"
        Lines[i] = tempStr
        continue
    token = Lines[i].split(" ")
    for j in token:
        if j in dataTypes:
            tempStr = ""
            tempStr = tempStr + \
                "if(1) { " + Lines[i] + \
                "} else { printf(\"Error\");}" + Lines[i]
            Lines[i] = tempStr
            break


for i in range(len(Lines)):
    Lines[i] = Lines[i] + "\n"

file1 = open('out8.c', 'w')
file1.writelines(Lines)
file1.close()
os.system('clang-format -style=Google -i ./out8.c')
