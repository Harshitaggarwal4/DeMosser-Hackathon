'''
First Updated: 18 Jun 2022
Last Updated: 23 Jun 2022
Function: 
'''
import os


def change_increment(input_file, output_file):
    os.system('clang-format -style=Google -i ./%s' % input_file)

    in1 = open(input_file, "r")
    out1 = open(output_file, "w")

    lines = in1.readlines()

    length = len(lines)
    for line_Ind in range(length + 1000):
        minecraft = len(lines)
        if line_Ind >= minecraft:
            break

        line = lines[line_Ind]
        # inc_Ind = line.find("++")
        # if inc_Ind == -1:
        #     continue

        line = line.replace("++;", "+=1;")
        lines[line_Ind] = line

    for line in lines:
        out1.write("%s" % line)

    in1.close()
    out1.close()
    os.system('clang-format -style=Google -i ./%s' % output_file)


if __name__ == '__main__':
    change_increment("out9.c", "out10.c")
