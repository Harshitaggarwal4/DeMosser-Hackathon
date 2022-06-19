'''
Developer: Yash Bhaskar || Harshit Aggarwal || Sreyas S
Date: 18 Jun 2022
Function: Changing all While loops to For loops.
'''
import re
import os
os.system('clang-format -style=Google -i ./out5.c')


with open('out5.c', 'r') as f:
    Lines = f.readlines()


for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()


for i in range(len(Lines)):
    if("while" in Lines[i]):
        condition = re.search('\((.*)\)', Lines[i])
        Lines[i] = "for(;" + condition.group(1) + ";) {"


for i in range(len(Lines)):
    Lines[i] = Lines[i] + "\n"

file1 = open('out6.c', 'w')
file1.writelines(Lines)
os.system('clang-format -style=Google -i ./out.c')
file1.close()
