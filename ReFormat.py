import os
os.system('clang-format -style=Google -i ./code2.c')

# changing int to long long int
with open('code.c','r') as f:
	Lines = f.readlines()


with open('code.c','r') as f:
    file1 = f.read()


# print(file1)
# print(type(Lines[1]))


for i in range(len(Lines)):
	Lines[i] = Lines[i].strip()



# Adding brackets after if, while, for,  if not present

for i in range(len(Lines)):
    if("if(" in Lines[i] or "while(" in Lines[i] or "for(" in Lines[i]):
        if("{" in Lines[i]):
            continue
        else:
            Lines[i] = Lines[i] + " {"
            if("while(" in Lines[i]):
                Lines[i+1] = Lines[i+1] + " }"
                continue
            if("for(" in Lines[i]):
                Lines[i+1] = Lines[i+1] + " }"
                continue
            Lines[i+1] = Lines[i+1] + " }"
            continue
    if("} else" in Lines[i]):
        if("{" in Lines[i]):
            continue
        else:
            if("if" in Lines[i]):
                Lines[i] = Lines[i] + " {"
                Lines[i+1] = Lines[i+1] + " }"
                continue
            Lines[i] = Lines[i] + " {"
            continue




for i in range(len(Lines)):
	Lines[i] = Lines[i] + "\n"


file1 = open('input1.c', 'w')
file1.writelines(Lines)
os.system('clang-format -style=Google -i ./input1.c')
file1.close()

with open('code.c','r') as f:
	Lines = f.readlines()


for i in range(len(Lines)):
    if("if(" in Lines[i] or "while(" in Lines[i] or "for(" in Lines[i]):
        if("{" in Lines[i]):
            continue
        else:
            Lines[i] = Lines[i] + " {"
            if("while(" in Lines[i]):
                Lines[i+1] = Lines[i+1] + " }"
                continue
            if("for(" in Lines[i]):
                Lines[i+1] = Lines[i+1] + " }"
                continue
            Lines[i+1] = Lines[i+1] + " }"
            continue
    if("else" in Lines[i]):
        if("{" in Lines[i]):
            continue
        else:
            Lines[i] = Lines[i] + " {"
            Lines[i+1] = Lines[i+1] + " }"
            continue




file1 = open('input1.c', 'w')
file1.writelines(Lines)
os.system('clang-format -style=Google -i ./input1.c')
file1.close()

for i in Lines:
	print(i)
