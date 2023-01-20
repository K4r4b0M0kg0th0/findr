import os
import csv
from typing import Tuple, List
from pdf_functions import findr
from input_validation import input_data

pdf_path, words, output_file = input_data()
total_words, unique_words, counts = findr(pdf_path, words, output_file)
if total_words != -1:
    print(f'The pdf contains {total_words} total words and {unique_words} unique words')
    if output_file:
        print(f'Results have been written to {output_file}')
else:
    print("An error occurred")