'''
Developer: Yash Bhaskar || Harshit Aggarwal
Date: 18 Jun 2022
Function: Adds #define one 1 & #define zero 0
'''
import os
os.system('clang-format -style=Google -i ./out10.c')

# changing int to long long int
with open('out10.c', 'r') as f:
    Lines = f.readlines()


for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()


Lines.insert(0, "#define one 1")
Lines.insert(0, "#define zero 0")


# adding *one+zero to alone integers
for i in range(len(Lines)):
    if("define" in Lines[i]):
        continue
    temp = Lines[i].split()
    for j in range(len(temp)):
        if(temp[j].isnumeric()):
            temp[j] = temp[j] + "*one+zero"
    tempLine = ""
    for j in temp:
        tempLine = tempLine + j + " "
    Lines[i] = tempLine


# Adding that to 9; , etc cases
for i in range(len(Lines)):
    if("define" in Lines[i]):
        continue
    tempLine = ""
    for j in range(len(Lines[i])):
        if(Lines[i][j].isnumeric()):
            if(j-1 >= 0 and j+1 < len(Lines[i])):
                if((Lines[i][j-1] == '+' or Lines[i][j-1] == '-' or Lines[i][j-1] == ' ' or Lines[i][j-1] == '[') and (Lines[i][j+1] == ']' or Lines[i][j+1] == ';' or Lines[i][j+1] == ' ')):
                    tempLine = tempLine + Lines[i][j] + "*one+zero"
                    continue
        tempLine = tempLine + Lines[i][j]
    Lines[i] = tempLine


# [200] cases
for i in range(len(Lines)):
    if("define" in Lines[i]):
        continue
    tempLine = ""
    for j in range(len(Lines[i])):
        if(Lines[i][j].isnumeric()):
            if(j-1 >= 0 and j+1 < len(Lines[i])):
                if((Lines[i][j-1] == '+' or Lines[i][j-1] == '-' or Lines[i][j-1] == ' ' or Lines[i][j-1] == '[') and (Lines[i][j+1] == ']' or Lines[i][j+1] == ';' or Lines[i][j+1] == ' ')):
                    tempLine = tempLine + Lines[i][j] + "*one+zero"
                    continue
        tempLine = tempLine + Lines[i][j]
    Lines[i] = tempLine


for i in range(len(Lines)):
    Lines[i] = Lines[i] + "\n"


file1 = open('out11.c', 'w')
file1.writelines(Lines)
file1.close()
os.system('clang-format -style=Google -i ./out11.c')
