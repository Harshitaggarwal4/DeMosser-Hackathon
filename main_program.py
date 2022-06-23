'''
First Updated: 23 Jun 2022
Last Updated: 23 Jun 2022
Function: Main program to run the Files
'''
import os

from add_random_stuff import add_random_stuff
from Array_Heap_declaration import array_heap_declaration
from changeIncrement import change_increment
from CharTypeChange import char_type_change
from FloatTypeChange import float_type_change
from goto import goto
from if1 import if1
from ifelse import ifelse
from ifToSwitch import if_to_switch
from IntTypeChange import int_type_change
from Mul_1_Add_zero import mul_1_add_zero
from ReFormat import reformat
from add_struct import struct_function
from whileToFor import while_to_for


def less_demoss(input_file, output_file):
    # Lesser Demossing, but not easily detectable

    file_name = input_file[:-2]+"_temp_"
    reformat(input_file, file_name+"1.c")
    array_heap_declaration(file_name+"1.c", file_name+"2.c")
    int_type_change(file_name+"2.c", file_name+"3.c")
    char_type_change(file_name+"3.c", file_name+"4.c")
    float_type_change(file_name+"4.c", file_name+"5.c")
    while_to_for(file_name+"5.c", file_name+"6.c")
    struct_function(file_name+"6.c", file_name+"7.c")
    if1(file_name+"7.c", file_name+"8.c")
    add_random_stuff(file_name+"8.c", file_name+"9.c")
    if_to_switch(file_name+"9.c", file_name+"10.c")
    change_increment(file_name+"10.c", output_file)
    os.system("rm %s*" % file_name)
    os.system('clang-format -style=Microsoft -i ./%s' % output_file)


def more_demoss(input_file, output_file):
    # More Demossing, but easily detectable

    file_name = input_file[:-2]+"_temp_"
    reformat(input_file, file_name+"1.c")
    array_heap_declaration(file_name+"1.c", file_name+"2.c")
    int_type_change(file_name+"2.c", file_name+"3.c")
    char_type_change(file_name+"3.c", file_name+"4.c")
    float_type_change(file_name+"4.c", file_name+"5.c")
    while_to_for(file_name+"5.c", file_name+"6.c")
    struct_function(file_name+"6.c", file_name+"7.c")
    if1(file_name+"7.c", file_name+"8.c")
    add_random_stuff(file_name+"8.c", file_name+"9.c")
    if_to_switch(file_name+"9.c", file_name+"10.c")
    change_increment(file_name+"10.c", file_name+"11.c")
    mul_1_add_zero(file_name+"11.c", output_file)
    os.system("rm %s*" % file_name)
    os.system('clang-format -style=Microsoft -i ./%s' % output_file)


if __name__ == '__main__':
    less_demoss("input.c", "final_output.c")
    more_demoss("input.c", "final_output_with_hashtag.c")

# Goto and Ifelse yet to be added
