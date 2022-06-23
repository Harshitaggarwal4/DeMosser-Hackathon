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
    reformat(input_file, "out.c")
    array_heap_declaration("out.c", "out2.c")
    int_type_change("out2.c", "out3.c")
    char_type_change("out3.c", "out4.c")
    float_type_change("out4.c", "out5.c")
    while_to_for("out5.c", "out6.c")
    struct_function("out6.c", "out7.c")
    if1('out7.c', 'out8.c')
    add_random_stuff("out8.c", "out8.c")
    if_to_switch("out8.c", "out9.c")
    change_increment("out9.c", output_file)
    os.system("rm out*")


def more_demoss(input_file, output_file):
    # More Demossing, but easily detectable
    reformat(input_file, "out.c")
    array_heap_declaration("out.c", "out2.c")
    int_type_change("out2.c", "out3.c")
    char_type_change("out3.c", "out4.c")
    float_type_change("out4.c", "out5.c")
    while_to_for("out5.c", "out6.c")
    struct_function("out6.c", "out7.c")
    if1('out7.c', 'out8.c')
    add_random_stuff("out8.c", "out8.c")
    if_to_switch("out8.c", "out9.c")
    change_increment("out9.c", "out10.c")
    mul_1_add_zero("out10.c", output_file)
    os.system("rm out*")


if __name__ == '__main__':
    less_demoss("input.c", "final_output.c")
    more_demoss("input.c", "final_output_with_hashtag.c")

# Goto and Ifelse yet to be added