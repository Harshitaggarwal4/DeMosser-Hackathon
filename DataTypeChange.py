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





# Changing the printf from %d to %lld
for i in range(len(Lines)):
	Lines[i] = (Lines[i].replace("%d","%lld"))



# Changing int to long long int 
for run in range(15):
	for i in range(len(Lines)):
		# Ignoring int main()
		if "int main()" in Lines[i]:
			continue
		for j in range(len(Lines[i])-3):
			if(Lines[i][j] == "i" and Lines[i][j+1] == "n" and Lines[i][j+2] == "t"):
				# int cant be at the end of the sentence
				if(j == range(len(Lines[i])-4)):
					continue

				if(Lines[i][j+3] == " " or Lines[i][j+3] == "*" or Lines[i][j+3] == ")"):
					# For int in the starting case
					if(j == 0):
						Lines[i] = Lines[i][:j] + "long long int" + Lines[i][j+3:]
						continue
						
					if(Lines[i][j-1] == "(" or Lines[i][j-1] == " " or Lines[i][j-1] == " "):
						# For long int or long long int case
						if(j-5 >= 0):
							if(Lines[i][j-5] == 'l' and Lines[i][j-4] == 'o' and Lines[i][j-3] == 'n' and Lines[i][j-2] == 'g'):
								if(j-6 >= 0 and (Lines[i][j-6] == " " or Lines[i][j-6] == "(")):
									continue
								if(j-6 < 0):
									continue;
						Lines[i] = Lines[i][:j] + "long long int" + Lines[i][j+3:]
						continue


# Changing char to unsigned char
for run in range(15):
	for i in range(len(Lines)):
		# Ignoring int main()
		if "int main()" in Lines[i]:
			continue
		for j in range(len(Lines[i])-4):
			if(Lines[i][j] == "c" and Lines[i][j+1] == "h" and Lines[i][j+2] == "a" and Lines[i][j+3] == "r"):
				# char cant be at the end of the sentence
				if(j == range(len(Lines[i])-5)):
					continue

				if(Lines[i][j+4] == " " or Lines[i][j+4] == "*" or Lines[i][j+4] == ")"):
					# For char in the starting case
					if(j == 0):
						Lines[i] = Lines[i][:j] + "unsigned char" + Lines[i][j+4:]
						continue
						
					if(Lines[i][j-1] == "(" or Lines[i][j-1] == " " or Lines[i][j-1] == " "):
						# For unsigned char case
						if(j-9 >= 0):
							if(Lines[i][j-9] == 'u' and Lines[i][j-8] == 'n' and Lines[i][j-7] == 's' and Lines[i][j-6] == 'i' and Lines[i][j-5] == 'g' and Lines[i][j-4] == 'n' and Lines[i][j-3] == 'e' and Lines[i][j-2] == 'd'):
								if(j-10 >= 0 and (Lines[i][j-10] == " " or Lines[i][j-10] == "(")):
									continue
								if(j-10 < 0):
									continue;
						Lines[i] = Lines[i][:j] + "unsigned char" + Lines[i][j+4:]
						continue


for i in range(len(Lines)):
	Lines[i] = Lines[i] + "\n"


file1 = open('input1.c', 'w')
file1.writelines(Lines)
file1.close()

for i in Lines:
	print(i)

