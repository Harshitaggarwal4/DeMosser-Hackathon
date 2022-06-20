#! /bin/bash
sudo apt-get install -y clang-format

python3 ReFormat.py
python3 Array_Heap_declaration.py
python3 IntTypeChange.py
python3 CharTypeChange.py
python3 FloatTypeChange.py
python3 whileToFor.py
python3 struct.py
python3 if1.py
python3 add_random_stuff.py
python3 ifToSwitch.py
python3 changeIncrement.py
mv out10.c final_output.c
rm out*

python3 ReFormat.py
python3 Array_Heap_declaration.py
python3 IntTypeChange.py
python3 CharTypeChange.py
python3 FloatTypeChange.py
python3 whileToFor.py
python3 struct.py
python3 if1.py
python3 add_random_stuff.py
python3 ifToSwitch.py
python3 changeIncrement.py
python3 Mul_1_Add_zero.py
mv out11.c final_output_with_hashtag.c
rm out*

sudo chmod +x moss.pl
./moss.pl ./input.c ./final_output.c
./moss.pl ./input.c ./final_output_with_hashtag.c
