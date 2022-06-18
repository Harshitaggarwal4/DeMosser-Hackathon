input_c = "input.c"
output_c = "out2.c"

in1 = open(input_c, "r")
out1 = open(output_c, "w")

lines = in1.readlines()

length = len(lines)
for line_Ind in range(length):
    line = lines[line_Ind]
    line = line.replace("++", "+=1")
    lines[line_Ind] = line

for line in lines:
    out1.write("%s"%line)

in1.close()
out1.close()