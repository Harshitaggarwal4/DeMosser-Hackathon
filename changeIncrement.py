import os
os.system('clang-format -style=Google -i ./out9.c')
input_c = "out9.c"
output_c = "out10.c"

in1 = open(input_c, "r")
out1 = open(output_c, "w")

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
os.system('clang-format -style=Google -i ./out10.c')
