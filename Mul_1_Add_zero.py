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

# for i in range(len(Lines)):
#     for j in range(len(Lines[i])-1):
#         if Lines[i][j].isdigit():
#             if j == 0:
#                 continue
#             if (Lines[i][j-1] == " " or Lines[i][j-1] == "-") and (Lines[i][j+1] == " " or Lines[i][j+1] == ";" or Lines[i][j+1] == ","):
#                 if(j-2 >= 0):
#                     if(Lines[i][j-2] != " "):
#                         continue
#                 Lines[i] = Lines[i][:j+1] + "*one+zero" + Lines[i][j+1:]


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


# for i in range(len(Lines)):
#     if("define" in Lines[i]):
#         continue
#     temp = Lines[i].split()
#     for j in range(len(temp)):
#         if(temp[j][:len(temp[j])-2].isnumeric() and temp[j][len(temp[j]-1)] == ";"):
#             temp[j] = temp[:len(temp[j])-2] + "*one+zero;"
#     tempLine = ""
#     for j in temp:
#         tempLine = tempLine + j + " "
#     Lines[i] = tempLine


for i in range(len(Lines)):
    if("define" in Lines[i]):
        continue
    temp = Lines[i].split()
    tempLine = ""
    for j in range(len(temp)):
        if(temp[j][len(temp[j])-1] == ';' and (temp[j][:(len(temp[j])-1)]).strip().isnumeric()):
            tempLine = tempLine + temp[j][:(len(temp[j])-1)] + "*one+zero;" + " "
        else:
            tempLine = tempLine + temp[j] + " "
    # for j in temp:
        # tempLine = tempLine + j + " "
    Lines[i] = tempLine



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

    # for j in temp:
        # tempLine = tempLine + j + " "
    Lines[i] = tempLine

for i in range(len(Lines)):
	Lines[i] = Lines[i] + "\n"


file1 = open('input2.c', 'w')
file1.writelines(Lines)
file1.close()

for i in Lines:
	print(i)

