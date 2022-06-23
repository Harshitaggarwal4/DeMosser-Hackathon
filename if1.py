'''
First Updated: 18 Jun 2022
Last Updated: 23 Jun 2022
Function: 
'''

import os


def if1(input_file, output_file):
    os.system('clang-format -style=Google -i ./%s' % input_file)

    with open(input_file, 'r') as f:
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

    file1 = open(output_file, 'w')
    file1.writelines(Lines)
    file1.close()
    os.system('clang-format -style=Google -i ./%s' % output_file)


if __name__ == '__main__':
    if1('out7.c', 'out8.c')
