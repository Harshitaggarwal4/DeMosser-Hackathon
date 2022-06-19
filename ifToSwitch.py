input_c = "out8.c"
output_c = "out9.c"

in1 = open(input_c, "r")
out1 = open(output_c, "w")

lines = in1.readlines()
if_expr = ""    # stores the expression of the if statement
if_body = ""    # stores the body of the if statement
else_body = ""
count = 0   # stores the bracket count
totalLines = len(lines)
if_Ind = -1
else_Ind = -1
elseIf_Ind = -1
flag = 0
if_starts = -1


for line_Ind in range(totalLines+1000):
    minecraft = len(lines)
    if line_Ind >= minecraft:
        break
    if lines[line_Ind] == "":
        continue
    # print(if_Ind)
    # print(line_Ind)
    line = lines[line_Ind]
    line_Length = len(line)
    # print(if_Ind)

    if flag == 1:
        # print("here")
        for char_Ind in range(len(line)):
            char = line[char_Ind]
            if char == "{":
                count += 1
            elif char == "}":
                count -= 1
            else_body += char
            if count == 0:  # end of if else
                for delLine_Ind in range(if_starts, line_Ind+1):
                    lines[delLine_Ind] = ""

                # switch_if_body = if_body.replace("}", "\n}")
                break_if_body_Ind = if_body.rindex("}")
                switch_break_text = "break;\n"
                switch_break_text += if_body[break_if_body_Ind::]
                sub_if_body = if_body[:break_if_body_Ind:]
                sub_if_body += switch_break_text

                switch_Command = "switch (%s) {\n" % if_expr
                switch_Command += "case 1: {\n" + sub_if_body + "\n"
                switch_Command += "default: {\n" + else_body + "\n}\n"
                lines.insert(if_starts, switch_Command)

                if_Ind = -1
                if_body = ""
                else_body = ""
                if_expr = ""
                count = 0
                else_Ind = -1
                elseIf_Ind = -1
                flag = 0
                if_starts = -1
                break
        continue

    if if_Ind != -1:
        elseIf_Ind = line.find("else if")
        if elseIf_Ind != -1 and count == 0:
            if_Ind = -1
            if_body = ""
            else_body = ""
            if_expr = ""
            count = 0
            else_Ind = -1
            elseIf_Ind = -1
            flag = 0
            if_starts = -1

        else_Ind = line.find("else {")
        if else_Ind != -1:
            if count == 0:  # it is an if-else condition
                flag = 1
                count = 1
                continue

        if count == 0:
            if_Ind = -1
            if_body = ""
            else_body = ""
            if_expr = ""
            count = 0
            else_Ind = -1
            elseIf_Ind = -1
            flag = 0
            if_starts = -1
            continue

        for char in line:
            if char == "{":
                count += 1
            elif char == "}":
                count -= 1
            if_body += char
            if count == 0:
                lines.insert(line_Ind, "")
                break
        continue

    if_Ind = line.find("if (")
    if if_Ind != -1:
        elseIf_Ind = line.find("else if")
        if elseIf_Ind != -1:
            if_Ind = -1
            if_body = ""
            else_body = ""
            if_expr = ""
            count = 0
            else_Ind = -1
            elseIf_Ind = -1
            if_starts = -1
            flag = 0
            continue
        else:
            if_starts = line_Ind
            subLine = line[if_Ind:line_Length-1:]
            if_expr_stInd = subLine.find("(")
            if_expr_endInd = subLine.rfind(")")
            # subLine_Tokens = subLine.split("(")
            # if_expr = subLine_Tokens[1].split(")")[0]
            if_expr = subLine[if_expr_stInd+1:if_expr_endInd:]
            count = 1
            continue

for i in lines:
    out1.write("%s" % i)
out1.close()
in1.close()
