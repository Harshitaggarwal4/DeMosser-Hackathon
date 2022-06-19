# DeMosser-Hackathon
De Mosses a given c code

## INSTALLATION AND USAGE PROCEDURE
1.  Download the zip, and extract the folder.
2.  save the code to be DeMossed in the file named ***input.c***
3.  on the terminal, change the working directory to the extracted directory
4.  run the command -

``` chmod +x shell.sh```  (only for the first time)

``` ./shell.sh ```

5.  the output will be stored in ***final_output.c*** and ***final_output_with_hashtag.c***
6.  the link for the Moss results will be displayed in the terminal


## FILE DESCRIPTIONS
1.  Array_heap_declaration.py - converts all the arrays declared in the given c program into heap allocations of respective datatype
2.  CharTypeChange.py - converts all the variables of datatype char into unsigned char
3.  FloatTypeChange.py - converts all the variables of float datatype into double
4.  IntTypeChange.py - converts all variables of integer datatype into long long
5.  ReFormat.py - formats the given c code according to usual standard
6.  Mul_1_Add_zero.py - during variable declarations, the RHS is multipled by 1 and 0 is added
7.  changeIncrement.py - increments done through the i++ method are changed to i+=1
8.  struct.py - creates random structures in the c program
9.  if1.py - randomly adds if(1) before statements that are certainly executed
10.  add_this.c - has random sort functions which will be used to implement sorting in the program
11.  add_random_stuff.py - uses the random sort function, to implement sorting in the program
12.  whileToFor.py - converts all the while loops into for loops
13.  ifToSwitch.py - converts if-else statements into switch-case conditions

## FUTURE IDEAS AND CURRENT IMPLEMENTATIONS
- [X] Convert **while** to **for**
- [X] change **int** to **long long**, (+other datatype changes)
- [X] convert **if-else** into **switch-case**
- [X] convert arrays into **mallocs** (freeing not implemented)
- [X] create a sort algorithm and use
- [X] **#define** random values
- [X] added a structure
- [X] Reformat the c file
- [ ] Create an interface to add the code to be demossed (half tick maybe ??)
- [ ] random testcase generator to review the final output
- [ ] split a function into multiple parts using program flow graph (PFG)
- [ ] change the order of execution of the program (PFG)
- [ ] ***Comments*** need to be handled.

