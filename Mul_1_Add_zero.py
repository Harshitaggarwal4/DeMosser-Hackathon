import os
os.system('clang-format -style=Google -i ./input.c')

# changing int to long long int
with open('code2.c','r') as f:
	Lines = f.readlines()


with open('code2.c','r') as f:
    file1 = f.read()


# print(file1)
# print(type(Lines[1]))

for i in range(len(Lines)):
	Lines[i] = Lines[i].strip()


Lines.insert(0,"#define one 1")
Lines.insert(0,"#define zero 0")

for i in range(len(Lines)):
    for j in range(len(Lines[i])-1):
        if Lines[i][j].isdigit():
            if j == 0:
                continue
            if (Lines[i][j-1] == " " or Lines[i][j-1] == "-") and (Lines[i][j+1] == " " or Lines[i][j+1] == ";" or Lines[i][j+1] == ","):
                if(j-2 >= 0):
                    if(Lines[i][j-2] != " "):
                        continue
                Lines[i] = Lines[i][:j+1] + "*one+zero" + Lines[i][j+1:]


for i in range(len(Lines)):
	Lines[i] = Lines[i] + "\n"


file1 = open('input2.c', 'w')
file1.writelines(Lines)
file1.close()

for i in Lines:
	print(i)

