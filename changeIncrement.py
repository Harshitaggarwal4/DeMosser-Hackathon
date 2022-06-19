input_c = "test.c"
output_c = "out2.c"

in1 = open(input_c, "r")
out1 = open(output_c, "w")

lines = in1.readlines()

length = len(lines)
for line_Ind in range(length):
    line = lines[line_Ind]
    inc_Ind = line.find("++")
    if inc_Ind == -1:
        continue
    newLine = line.split("++")
    # print(newLine)
    if newLine[1][0].isalpha():
        newLine[1] = newLine[1].replace(","," ")
        newLine[1] = newLine[1].replace("["," ")
        newLine[1] = newLine[1].replace("("," ")
        newLine[1] = newLine[1].replace("]"," ")
        newLine[1] = newLine[1].replace(")"," ")
        newLine[1] = newLine[1].replace("{"," ")
        newLine[1] = newLine[1].replace("}"," ")
        newLine[1] = newLine[1].replace("\""," ")
        newLine[1] = newLine[1].replace("'"," ")
        newLine[1] = newLine[1].replace("="," ")
        newLine[1] = newLine[1].replace("+"," ")
        newLine[1] = newLine[1].replace("-"," ")
        newLine[1] = newLine[1].replace("*"," ")
        newLine[1] = newLine[1].replace("/"," ")
        newLine[1] = newLine[1].replace(";"," ")

        newSub = newLine[1].split()
        name = newSub[0]
        line = line.replace("++%s"%name, "%s+=1"%name)

    else:

        newLine[0] = newLine[0].replace("["," ")
        newLine[0] = newLine[0].replace("("," ")
        newLine[0] = newLine[0].replace("]"," ")
        newLine[0] = newLine[0].replace(")"," ")
        newLine[0] = newLine[0].replace("{"," ")
        newLine[0] = newLine[0].replace("}"," ")
        newLine[0] = newLine[0].replace("\""," ")
        newLine[0] = newLine[0].replace("'"," ")
        newLine[0] = newLine[0].replace(","," ")
        newLine[0] = newLine[0].replace("="," ")
        newLine[0] = newLine[0].replace("+"," ")
        newLine[0] = newLine[0].replace("-"," ")
        newLine[0] = newLine[0].replace("*"," ")
        newLine[0] = newLine[0].replace("/"," ")
        newLine[0] = newLine[0].replace(";"," ")

        print(newLine[0])
        newSub = newLine[0].split()
        name = newSub[-1]
        line = line.replace("++", "+=0")
        lines.insert(line_Ind+1, "%s+=1;\n"%name)

    lines[line_Ind] = line

for line in lines:
    out1.write("%s"%line)

in1.close()
out1.close()
