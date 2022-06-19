import os
from tracemalloc import start
os.system('clang-format -style=Google -i ./code.c')

# changing int to long long int
with open('code.c','r') as f:
	Lines = f.readlines()


with open('code.c','r') as f:
    file1 = f.read()


# print(file1)
# print(type(Lines[1]))


for i in range(len(Lines)):
	Lines[i] = Lines[i].strip()


import re

startIdx = 0
endIdx = 0
endBracketIdx = 0
check = 0
# Changing loops of if else into Switch Case
# Run the Reformat code first

counter = 0
level1 = 0
level2 = 10
for i in range(len(Lines)):
    if("if (" in Lines[i]):
        counter = counter + 1
        if(";" in Lines[i] or "else" in Lines[i] or not("{" in Lines[i])):
            startIdx = 0
            endIdx = 0
            endBracketIdx = 0
            check = 0
            level1 = 0
            level2 = 10
            continue
        condition1 = re.search('\((.*)\)', Lines[i])
        startIdx = i
        level1 = 5
        level2 = 5
    if(counter == 2):
        break
    if("else if" in Lines[i]):
        check = 1
    if("else {" in Lines[i]):
        endIdx = i
        # condition2 = re.search('((.*))', Lines[i])
        if(startIdx == 0):
            startIdx = 0
            endIdx = 0
            check = 0
            level1 = 0
            level2 = 10
    if(check == 1):
        check = 0
        startIdx = 0
        endIdx = 0
        level1 = 0
        level2 = 10
    for z in Lines[i]:
        if(z == '}'):
            level2 = level2 - 1
        if(z == "{"):
            level2 = level2 + 1
    if(check == 0 and startIdx != 0 and endIdx != 0 and level1 == level2):
        print(condition1.group(1))
        Lines[startIdx] = "switch(" + condition1.group(1) + ") { case 1: {"
        Lines[endIdx-1] = Lines[endIdx-1] + " break; }"
        print(startIdx)
        Lines[endIdx] = "default: {"
        count = level2
        for j in range(endIdx+1,len(Lines),1):
            for z in range(len(Lines[j])):
                if(Lines[j][z] == "{"):
                    count = count + 1
                if(Lines[j][z] == "}"):
                    count = count - 1
                    if(count == level2-1):
                        Lines[j] = Lines[j][:z] + " break; }}"
                        startIdx = 0
                        endIdx = 0
                        check = 0
                        level1 = 0
                        level2 = 10
                        break
        






for i in range(len(Lines)):
	Lines[i] = Lines[i] + "\n"


file1 = open('input1.c', 'w')
file1.writelines(Lines)
file1.close()

for i in Lines:
	print(i)

