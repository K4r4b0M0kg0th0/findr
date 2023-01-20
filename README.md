# Nyaka

This program allows you to find and count the occurrences of specified words in a pdf file. It can also output the results to a csv file. The program supports different match types (Exact, Partial, Regex) and return types (Tuple, Dict).

## Getting Started

These instructions will help you to run the program on your local machine.

### Prerequisites

- Python 3.x
- PyPDF2
- argparse

### Installing

You can install the required libraries using pip: pip install pypdf2 argparse

### Running the Program

You can run the program by invoking the main.py script: python main.py

The program will prompt you for the path to the pdf file, the word(s) to search for, and the path for the output file (if desired). The match_type and return_type can be passed as optional arguments.

python main.py -h for more information about the command-line arguments.

The program will print the total number of words and unique words in the pdf file, and the counts for each specified word. If an output file is specified, the results will also be written to the csv file.

## Built With

- [PyPDF2](https://pythonhosted.org/PyPDF2/) - A library to work with pdf files
- [argparse](https://docs.python.org/3/library/argparse.html) - A library for command-line parsing

## Authors

- **K4r4b0**
