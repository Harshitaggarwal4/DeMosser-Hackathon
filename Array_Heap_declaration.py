import os
os.system('clang-format -style=Google -i ./out.c')
input_c = "out.c"
output_c = "out2.c"

in1 = open(input_c, "r")
out1 = open(output_c, "w")

lines = in1.readlines()
dataTypes = ["char", "float", "double", "int",
             "long", "long int", "long long", "long long int"]


def convertArrToHeap():
    level = 0
    for line_Index in range(len(lines)):
        line = lines[line_Index]

        bracket_Ind = line.find("(", 0, len(line))
        if bracket_Ind == -1:
            pass
        else:
            continue

        comment_Ind = line.find("//", 0, len(line))
        if comment_Ind == -1:
            pass
        else:
            line = line[:comment_Ind]

        ind_o = -1  # stores the index where the '[' is present
        ind_c = -1  # stores the index where the brackets are closed ']'
        # stores teh index where the datatype (if present) is present
        ind1 = -1
        size = 0    # size of the declared array
        used_DT = "int"

        for type in dataTypes:
            length = len(line)

            ind_o = line.find("[", 0, length)
            if (ind_o == -1):
                break
            else:
                ind1 = line.find(type, 0, length)
                if (ind1 != -1):
                    used_DT = type
                    break

        newLine_Ind_o2 = line.find("{", 0, length)
        if newLine_Ind_o2 != -1:
            if line.find("}", 0, length) == -1:
                level += 1
            continue

        newLine_Ind_o2 = line.find("}", 0, length)
        if newLine_Ind_o2 != -1:
            if line.find("{", 0, length) == -1:
                level -= 1
            continue

        if (ind_o == -1 or ind1 == -1):     # if square brackets arent present, no arrays are declared
            continue

        if level == 0:
            continue

        newLines = line.split(",")
        numNewLines = len(newLines)
        for newLine_Ind in range(numNewLines):
            if newLine_Ind == 0:
                newLines[newLine_Ind] = newLines[newLine_Ind] + ";\n"
                continue
            elif (newLine_Ind == numNewLines-1):
                newLines[newLine_Ind] = used_DT + " " + newLines[newLine_Ind]
                continue
            newLines[newLine_Ind] = used_DT + \
                " " + newLines[newLine_Ind] + ";\n"

        for newLineI_ind in range(numNewLines):
            newLineI = newLines[newLineI_ind]
            newLine_Ind_o = newLineI.find("[", 0, length)
            # print(newLineI)

            if newLine_Ind_o == -1:
                continue

            newLine_Ind_o2 = newLineI.find("=", 0, length)
            if newLine_Ind_o2 != -1:
                continue

            newLine_Ind_o2 = newLineI.find("[", newLine_Ind_o+1, length)
            if newLine_Ind_o2 != -1:
                continue

            newLine_Ind_o2 = newLineI.find("{", 0, length)
            if newLine_Ind_o2 != -1:
                continue

            newLine_Ind_c = newLineI.find("]", 0, length)
            size_Var = newLineI[newLine_Ind_o+1:newLine_Ind_c:]
            size_Var = size_Var.split()
            size_var_Name = ""
            for characters in size_Var:
                size_var_Name += characters
            # print("size = ",size_var_Name)

            subString1 = newLineI[0:newLine_Ind_o+1:]
            subString2 = newLineI[newLine_Ind_c::]
            # print("old = ",newLineI)
            tempNewLine = subString1 + size_var_Name + subString2
            # newLineI.replace(subString1, size_var_Name)
            newLineI = tempNewLine
            # print("new = ",newLineI)
            # print(ind_c)
            currLine = newLineI.replace("[", " ")
            currLine = currLine.replace("]", " ")
            currLine = currLine.replace(",", " ")
            currLine = currLine.split()
            # print(currLine)
            # stores the value between the brackets
            sub = newLineI[newLine_Ind_o+1:newLine_Ind_c:]
            # print(sub)
            sub = sub.strip()
            try:
                size = int(sub)
            except:
                size = size_var_Name
            # print(size)

            arr_IndSize = currLine.index(str(size))
            name = currLine[arr_IndSize-1]
            newLine = used_DT+"* " + name + \
                " = (" + used_DT + "*) malloc(sizeof(" + \
                used_DT + ")*" + str(size) + ");\n"
            checkAlloc = 'if (%s == NULL) {\nprintf("Heap exhausted!!!\\n");\nexit(0);\n}\n' % name
            newLine += checkAlloc
            newLines[newLineI_ind] = newLine

        numNewLines = len(newLines)
        for changedLines_Ind in range(numNewLines):
            if (changedLines_Ind == 0):
                lines[line_Index] = newLines[changedLines_Ind]
                continue
            lines.insert(line_Index+1, newLines[changedLines_Ind])
            line_Index += 1


convertArrToHeap()
convertArrToHeap()
# print(lines)
for item in lines:
    out1.write("%s" % item)

out1.close()
in1.close()
os.system('clang-format -style=Google -i ./out2.c')
