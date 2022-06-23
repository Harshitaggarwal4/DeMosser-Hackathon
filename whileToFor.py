'''
First Updated: 18 Jun 2022
Last Updated: 23 Jun 2022
Function: Changing all While loops to For loops.
'''
import re
import os


def while_to_for(input_file, output_file):
    os.system('clang-format -style=Google -i ./%s' % input_file)

    with open(input_file, 'r') as f:
        Lines = f.readlines()

    for i in range(len(Lines)):
        Lines[i] = Lines[i].strip()

    for i in range(len(Lines)):
        if("while" in Lines[i]):
            condition = re.search('\((.*)\)', Lines[i])
            Lines[i] = "for(;" + condition.group(1) + ";) {"

    for i in range(len(Lines)):
        Lines[i] = Lines[i] + "\n"

    file1 = open(output_file, 'w')
    file1.writelines(Lines)
    file1.close()
    os.system('clang-format -style=Google -i ./%s' % output_file)


if __name__ == '__main__':
    while_to_for("out5.c", "out6.c")
