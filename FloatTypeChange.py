import os
os.system('clang-format -style=Google -i ./input.c')

# changing int to long long int
with open('code2.c','r') as f:
	Lines = f.readlines()


with open('code2.c','r') as f:
    file1 = f.read()


# print(file1)
# print(type(Lines[1]))


for i in range(len(Lines)):
	Lines[i] = Lines[i].strip()


# Changing the printf from %f to %lf
for i in range(len(Lines)):
	Lines[i] = (Lines[i].replace("%f","%.6lf"))



# Changing float to double
for run in range(15):
	for i in range(len(Lines)):
		# Ignoring int main()
		if "int main()" in Lines[i]:
			continue
		for j in range(len(Lines[i])-5):
			if(Lines[i][j] == "f" and Lines[i][j+1] == "l" and Lines[i][j+2] == "o" and Lines[i][j+3] == "a" and Lines[i][j+4] == "t"):
				# float cant be at the end of the sentence
				if(j == range(len(Lines[i])-6)):
					continue

				if(Lines[i][j+5] == " " or Lines[i][j+5] == "*" or Lines[i][j+5] == ")"):
					# For float in the starting case
					if(j == 0):
						Lines[i] = Lines[i][:j] + "double" + Lines[i][j+5:]
						continue
						
					if(Lines[i][j-1] == "(" or Lines[i][j-1] == " " or Lines[i][j-1] == " "):
						Lines[i] = Lines[i][:j] + "double" + Lines[i][j+5:]
						continue



for i in range(len(Lines)):
	Lines[i] = Lines[i] + "\n"


file1 = open('input1.c', 'w')
file1.writelines(Lines)
file1.close()

for i in Lines:
	print(i)
