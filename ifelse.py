'''
First Updated: 23 Jun 2022
Last Updated: 23 Jun 2022
Function: changes ifelse to if
'''
import os
import re


def ifelse(input_file, output_file):
    os.system('clang-format -style=Google -i ./%s' % input_file)

    with open(input_file, 'r') as f:
        Lines = f.readlines()

    for i in range(len(Lines)):
        Lines[i] = Lines[i].strip()

    idx_main = -1
    for i in range(len(Lines)):
        if('int main()' in Lines[i]):
            idx_main = i
            break

    if(idx_main == -1):
        return

    # Here i will be storing the if conditions with key as level
    ifConditions = {}
    for i in range(20):
        ifConditions[i] = []

    level = 0

    for i in range(len(Lines)):
        for j in range(len(Lines[i])):
            if(Lines[i][j] == "{"):
                level = level + 1
            if(Lines[i][j] == "}"):
                level = level - 1
        
        # Clearing the inner level conditions whose scope are over
        for z in range(level+1, 20):
            ifConditions[z] = []
        
        # Now we are at level stored in the level
        if("else if (" in Lines[i]):
            condition = re.search('\((.*)\)', Lines[i])
            condition_str = "(" + condition.group(0) + ")"
            newCondition = "("
            for z in range(len(ifConditions[level])):
                newCondition = newCondition + "!" + \
                    ifConditions[level][z] + " && "
            if(newCondition == "("):
                newCondition = condition_str
            else:
                newCondition = newCondition + "1)"
                newFinalCondition = condition_str + " && " + newCondition
            Lines[i] = "} if (" + newFinalCondition + ") {"
            ifConditions[level].append(condition_str)
        elif("if (" in Lines[i]):
            condition = re.search('\((.*)\)', Lines[i])
            condition_str = "(" + condition.group(0) + ")"
            ifConditions[level] == []
            ifConditions[level].append(condition_str)
        elif("else {" in Lines[i]):
            newCondition = "("
            for z in range(len(ifConditions[level])):
                newCondition = newCondition + "!" + \
                    ifConditions[level][z] + " && "
            newCondition = newCondition + "1)"
            newFinalCondition = newCondition
            Lines[i] = "} if (" + newFinalCondition + ") {"
            ifConditions[level] = []

    for i in range(len(Lines)):
        Lines[i] = Lines[i] + "\n"

    file1 = open(output_file, 'w')
    file1.writelines(Lines)
    file1.close()
    os.system('clang-format -style=Google -i ./%s' % output_file)


if __name__ == '__main__':
    ifelse("out.c", "out.c")
