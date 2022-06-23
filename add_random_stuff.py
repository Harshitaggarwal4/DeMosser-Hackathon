'''
First Updated: 18 Jun 2022
Last Updated: 23 Jun 2022
Function: Adds some random functions on the top and adds some random variables throughout the code.
'''

import os


def add_random_stuff(input_file, output_file):

    os.system('clang-format -style=Google -i ./%s' % input_file)
    with open(input_file, 'r') as f:
        Lines = f.readlines()

    index = 0

    for i in Lines:
        i.strip()
        if i == "int main() {\n":
            break
        index = index+1

    x = []
    for i in range(index):
        x.append(Lines[i])

    with open('add_this.c', 'r') as f:
        add = f.readlines()
    for i in add:
        x.append(i)
    for i in range(len(Lines)-index):
        x.append(Lines[i+index])

    file1 = open(output_file, 'w')
    file1.writelines(x)
    file1.close()

    os.system('clang-format -style=Google -i ./%s' % output_file)

    with open(output_file, 'r') as f:
        x = f.readlines()

    count = 0
    c = 0

    for i in x:
        if count % 15 == 0:
            if count != 0:
                string = str(c)
                x.insert(count, "long long int " + "_querry___"+string+";")
                count = count+1
                c = c+1
        count = count+1

    file1 = open(output_file, 'w')
    file1.writelines(x)
    file1.close()

    os.system('clang-format -style=Google -i ./%s' % output_file)
    with open(output_file, 'r') as f:
        x = f.readlines()

    index = 0

    for i in x:
        i.strip()
        if i == "int main() {\n":
            break
        index = index+1

    index = index+1
    x.insert(index, "long long int array_my_own_array[9]={3,2,1,6,5,4,9,8,7};")
    index = index+1
    x.insert(index, "merge_sorting_sort(array_my_own_array, 0, 8);")
    index = index+1

    file1 = open(output_file, 'w')
    file1.writelines(x)
    file1.close()

    os.system('clang-format -style=Google -i ./%s' % output_file)
    with open(output_file, 'r') as f:
        x = f.readlines()

    index = 0
    for i in x:
        i.strip()
        if i == "int main() {\n":
            break
        index = index+1

    x.insert(index, "int solve_my_code_please(){")
    index = index+1
    x.pop(index)
    x.append("int main(){solve_my_code_please();return 0;}")

    file1 = open(output_file, 'w')
    file1.writelines(x)
    file1.close()

    os.system('clang-format -style=Google -i ./%s' % output_file)


if __name__ == '__main__':
    add_random_stuff("out8.c", "out8.c")
