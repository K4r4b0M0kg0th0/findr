import os
import argparse
from pdf_functions import EXACT_MATCH, PARTIAL_MATCH, REGEX_MATCH

def validate_input():
    parser = argparse.ArgumentParser(description='Find and count the occurrences of specified words in a pdf file')
    parser.add_argument('pdf_path', help='The path to the pdf file')
    parser.add_argument('words', help='The word(s) to search for, separated by commas')
    parser.add_argument('-o', '--output', help='The path for the output file')
    parser.add_argument('-m', '--match_type', choices=[EXACT_MATCH, PARTIAL_MATCH, REGEX_MATCH], default=EXACT_MATCH, help='The type of match to use (exact, partial, regex)')
    parser.add_argument('-r', '--return_type', choices=['tuple', 'dict'], default='tuple', help='The type of return value (tuple, dict)')
    args = parser.parse_args()

    pdf_path = args.pdf_path
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"{pdf_path} not found.")
    words = args.words.strip().split(',')
    output_file = args.output
    match_type = args.match_type
    return_type = args.return_type
    return pdf_path, words, output_file, match_type, return_type
