'''
Developer: Yash Bhaskar || Harshit Aggarwal
Date: 20 Jun 2022
Function: Adds random Goto calls inside the int main
'''
import os
os.system('clang-format -style=Google -i ./out.c')


with open('out.c', 'r') as f:
    Lines = f.readlines()


for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()


idx_main = -1
for i in range(len(Lines)):
    if('int main()' in Lines[i]):
        idx_main = i
        break


if(idx_main == -1):
    exit()


var_name = 1

for i in range(idx_main+1, len(Lines)):
    if(i % 30 == 0):
        gotoStr = ""
        gotoStr = gotoStr + "goto " + "gotoStr" + str(var_name+1) + "; "
        gotoStr = gotoStr + "gotoStr" + str(var_name) + ": ;"
        gotoStr = gotoStr + "int " + "gotoStr" + \
            str(var_name) + " = " + str(i) + "; "
        gotoStr = gotoStr + "gotoStr" + \
            str(var_name) + " = " + "gotoStr" + str(var_name) + \
            "*" + "gotoStr" + str(var_name) + "; "
        gotoStr = gotoStr + "goto " + "gotoStr" + str(var_name+2) + "; "
        gotoStr = gotoStr + "gotoStr" + str(var_name+1) + ": ;"
        gotoStr = gotoStr + "int " + "gotoStr" + \
            str(var_name+1) + " = " + str(i+20) + "; "
        gotoStr = gotoStr + "gotoStr" + str(var_name+1) + " = " + "gotoStr" + str(
            var_name+1) + "*" + "gotoStr" + str(var_name+1) + "; "
        gotoStr = gotoStr + "goto " + "gotoStr" + str(var_name) + "; "
        gotoStr = gotoStr + "gotoStr" + str(var_name+2) + ": ;"
        '''
        goto try2;
        try1:
        int try1 = 56;
        try1 = try1*try1;
        goto try3;
        try2:
        int try2 = 36;
        try2 = try2*try2;
        goto try1;
        try3:
        '''
        Lines.insert(i, gotoStr)
        var_name = var_name+3


for i in range(len(Lines)):
    Lines[i] = Lines[i] + "\n"


file1 = open('out.c', 'w')
file1.writelines(Lines)
file1.close()
os.system('clang-format -style=Google -i ./out.c')
