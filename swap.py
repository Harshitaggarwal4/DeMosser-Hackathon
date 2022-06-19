import os
from tracemalloc import start
os.system('clang-format -style=Google -i ./input2.c')

import re
def processString(txt):
  txt = re.sub('[\',/<\">?:''\"\\|[]=+~!@#$%^&*()`]', ' ', txt)
  return txt


with open('input2.c','r') as f:
	Lines = f.readlines()



for i in range(len(Lines)):
    Lines[i] = processString(Lines[i])



for i in range(len(Lines)):
	Lines[i] = Lines[i].strip()



for i in range(len(Lines)-1):
    if(Lines[i] == "" or Lines[i+1] == ""):
        continue
    if("return" in Lines[i] or "return" in Lines[i+1]):
        continue
    flag = 1
    if(i%2 == 0):
        continue
    for j in Lines[i]:
        if(j == "{" or j == "}"):
            flag = 0
            break
    if(flag == 0):
        continue
    if(Lines[i][len(Lines[i])-1] != ";"): 
        tempList1 = Lines[i].split(" ")
        tempList2 = Lines[i+1].split(" ")
        chk = 0
        for j in tempList1:
            for z in tempList2:
                if(j == z):
                    chk = 1
                    break
        if(chk == 0):
            temp = Lines[i]
            Lines[i] = Lines[i+1]
            Lines[i+1] = temp

for i in range(len(Lines)):
	Lines[i] = Lines[i] + "\n"

file1 = open('out.c', 'w')
file1.writelines(Lines)
os.system('clang-format -style=Google -i ./out.c')
file1.close()

