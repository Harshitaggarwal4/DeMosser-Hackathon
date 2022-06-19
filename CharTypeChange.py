'''
Developer: Yash Bhaskar || Harshit Aggarwal
Date: 18 Jun 2022
Function: Changes all the char Datatypes declared as unsigned char.
'''
import os
os.system('clang-format -style=Google -i ./out3.c')

# changing int to long long int
with open('out3.c', 'r') as f:
    Lines = f.readlines()


for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()


# Changing char to unsigned char
for run in range(15):
    for i in range(len(Lines)):
        # Ignoring int main()
        if "int main()" in Lines[i]:
            continue
        for j in range(len(Lines[i])-4):
            if(Lines[i][j] == "c" and Lines[i][j+1] == "h" and Lines[i][j+2] == "a" and Lines[i][j+3] == "r"):
                # char cant be at the end of the sentence
                if(j == range(len(Lines[i])-5)):
                    continue

                if(Lines[i][j+4] == " " or Lines[i][j+4] == "*" or Lines[i][j+4] == ")"):
                    # For char in the starting case
                    if(j == 0):
                        Lines[i] = Lines[i][:j] + \
                            "unsigned char" + Lines[i][j+4:]
                        continue

                    if(Lines[i][j-1] == "(" or Lines[i][j-1] == " " or Lines[i][j-1] == " "):
                        # For unsigned char case
                        if(j-9 >= 0):
                            if(Lines[i][j-9] == 'u' and Lines[i][j-8] == 'n' and Lines[i][j-7] == 's' and Lines[i][j-6] == 'i' and Lines[i][j-5] == 'g' and Lines[i][j-4] == 'n' and Lines[i][j-3] == 'e' and Lines[i][j-2] == 'd'):
                                if(j-10 >= 0 and (Lines[i][j-10] == " " or Lines[i][j-10] == "(")):
                                    continue
                                if(j-10 < 0):
                                    continue
                        Lines[i] = Lines[i][:j] + \
                            "unsigned char" + Lines[i][j+4:]
                        continue


for i in range(len(Lines)):
    Lines[i] = Lines[i] + "\n"


file1 = open('out4.c', 'w')
file1.writelines(Lines)
file1.close()
