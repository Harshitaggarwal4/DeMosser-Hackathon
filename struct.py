'''
Developer: Yash Bhaskar || Harshit Aggarwal
Date: 18 Jun 2022
Function: Adding a structure to the code.
'''
import os
os.system('clang-format -style=Google -i ./out6.c')


with open('out6.c', 'r') as f:
    Lines = f.readlines()


for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()


Hash_Hashing = "struct Hash_Hashing { char Hash[50]; int frequency; float value; };"


for i in range(len(Lines)):
    if("int main()" in Lines[i]):
        Lines.insert(i, Hash_Hashing)
        break

temp = 0
chk = 0
for i in range(len(Lines)):
    if("int main()" in Lines[i]):
        Lines.insert(i+1, "struct Hash_Hashing Hash_Hashing1,Hash_Hashing2;")
        chk = 1
    if(chk == 1):
        temp = temp+1
    if(temp == 5):
        Lines.insert(i, '*Hash_Hashing1.Hash="Key1";')
    if(temp == 11):
        Lines.insert(i, "Hash_Hashing1.frequency=0;")
    if(temp == 19):
        Lines.insert(i, "Hash_Hashing1.value = 1;")
    if(temp == 25):
        Lines.insert(i, '*Hash_Hashing2.Hash="Key2";')
    if(temp == 33):
        Lines.insert(i, "Hash_Hashing2.frequency=0;")
    if(temp == 40):
        Lines.insert(i, "Hash_Hashing2.value=2;")


for i in range(len(Lines)):
    Lines[i] = Lines[i] + "\n"

file1 = open('out7.c', 'w')
file1.writelines(Lines)
os.system('clang-format -style=Google -i ./out7.c')
file1.close()
