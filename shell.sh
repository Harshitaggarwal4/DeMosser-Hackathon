#! /bin/bash
sudo apt-get install -q -y clang-format > temp_output_installation
rm temp_output_installation

if [ $# -le 2 ]
    then
        python3 main_program.py
    else
        python3 main_program.py $1 $2 $3
fi

sudo chmod +x moss.pl

if [ $# -le 2 ]
    then
        ./moss.pl ./input.c ./final_output.c
        ./moss.pl ./input.c ./final_output_with_hashtag.c
    else
        ./moss.pl $1 $2
        ./moss.pl $1 $3

fi
