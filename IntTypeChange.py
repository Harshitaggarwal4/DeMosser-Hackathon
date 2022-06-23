'''
First Updated: 18 Jun 2022
Last Updated: 23 Jun 2022
Function: Changes all the int Datatypes declared as long long int.
'''
import os


def int_type_change(input_file, output_file):
    os.system('clang-format -style=Google -i ./%s' % input_file)

    with open(input_file, 'r') as f:
        Lines = f.readlines()

    for i in range(len(Lines)):
        Lines[i] = Lines[i].strip()

    # Changing the printf from %d to %lld
    for i in range(len(Lines)):
        Lines[i] = (Lines[i].replace("%d", "%lld"))

    # Changing int to long long int
    for run in range(15):
        for i in range(len(Lines)):
            # Ignoring int main()
            if "int main()" in Lines[i]:
                continue
            for j in range(len(Lines[i])-3):
                if(Lines[i][j] == "i" and Lines[i][j+1] == "n" and Lines[i][j+2] == "t"):
                    # int cant be at the end of the sentence
                    if(j == range(len(Lines[i])-4)):
                        continue

                    if(Lines[i][j+3] == " " or Lines[i][j+3] == "*" or Lines[i][j+3] == ")"):
                        # For int in the starting case
                        if(j == 0):
                            Lines[i] = Lines[i][:j] + \
                                "long long int" + Lines[i][j+3:]
                            continue

                        if(Lines[i][j-1] == "(" or Lines[i][j-1] == " " or Lines[i][j-1] == " "):
                            # For long int or long long int case
                            if(j-5 >= 0):
                                if(Lines[i][j-5] == 'l' and Lines[i][j-4] == 'o' and Lines[i][j-3] == 'n' and Lines[i][j-2] == 'g'):
                                    if(j-6 >= 0 and (Lines[i][j-6] == " " or Lines[i][j-6] == "(")):
                                        continue
                                    if(j-6 < 0):
                                        continue
                            Lines[i] = Lines[i][:j] + \
                                "long long int" + Lines[i][j+3:]
                            continue

    for i in range(len(Lines)):
        Lines[i] = Lines[i] + "\n"

    file1 = open(output_file, 'w')
    file1.writelines(Lines)
    file1.close()
    os.system('clang-format -style=Google -i ./%s' % output_file)


if __name__ == '__main__':
    int_type_change("out2.c", "out3.c")
