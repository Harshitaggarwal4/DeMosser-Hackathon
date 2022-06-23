'''
First Updated: 18 Jun 2022
Last Updated: 23 Jun 2022
Function: Adds/Complete the brackets {} in case of if(), for(), while() loops in the code
'''
import os

import os


def reformat(input_file, output_file):
    os.system('clang-format -style=Google -i ./%s' % input_file)

    # changing int to long long int
    with open(input_file, 'r') as f:
        Lines = f.readlines()

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

    file1 = open(output_file, 'w')
    file1.writelines(Lines)
    file1.close()
    os.system('clang-format -style=Google -i ./%s' % output_file)

    with open(output_file, 'r') as f:
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

    file1 = open(output_file, 'w')
    file1.writelines(Lines)
    file1.close()
    os.system('clang-format -style=Google -i ./%s' % output_file)


if __name__ == '__main__':
    reformat("input.c", "out.c")
