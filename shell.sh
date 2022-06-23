#! /bin/bash
sudo apt-get install -q -y clang-format > temp_output_installation
rm temp_output_installation

python3 main_program.py

sudo chmod +x moss.pl
./moss.pl ./input.c ./final_output.c
./moss.pl ./input.c ./final_output_with_hashtag.c
