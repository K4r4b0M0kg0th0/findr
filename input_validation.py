import os

def input_data():
    pdf_path = input("Enter the path to the pdf file: ")
    if not pdf_path:
        raise ValueError("pdf_path cannot be empty")
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"{pdf_path} not found.")
    words = input("Enter the word(s) to search for separated by commas: ").strip().split(',')
    if not words:
        raise ValueError("words cannot be empty")
    output_file = input("Enter the path for the output file: ")
    return pdf_path, words, output_file

