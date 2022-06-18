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
for i in range(len(Lines)):
    if("if (" in Lines[i]):
        condition1 = re.search('\((.*)\)', Lines[i])
        startIdx = i
    if("else if" in Lines[i]):
        check = 1
    if("else {" in Lines[i]):
        endIdx = i
        # condition2 = re.search('((.*))', Lines[i])
        if(startIdx == 0):
            startIdx = 0
            endIdx = 0
            check = 0
    if(check == 1):
        check = 0
        startIdx = 0
        endIdx = 0
    if(check == 0 and startIdx != 0 and endIdx != 0):
        print(condition1.group(1))
        Lines[startIdx] = "switch(" + condition1.group(1) + ") { case 1:"
        Lines[endIdx-1] = Lines[endIdx-1] + " break;"
        Lines[endIdx] = "default:"
        startIdx = 0
        endIdx = 0
        chcek = 0
        # count = 1
        # for j in range(endIdx,len(Lines),1):
        #     for z in range(Lines[j]):
        #         if(Lines[j][z] == "{"):
        #             count = count + 1
        #         if(Lines[j][z] == "}"):
        #             count = count - 1
        #             if(count == 0):
        #                 Lines[j] = Lines[j][:z] + " break;"







for i in range(len(Lines)):
	Lines[i] = Lines[i] + "\n"


file1 = open('input1.c', 'w')
file1.writelines(Lines)
file1.close()

for i in Lines:
	print(i)

