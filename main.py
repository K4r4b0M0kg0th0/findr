import os
import PyPDF2
import csv
from typing import List, Tuple

def findr(pdf_path: str, words: List[str], output_file: str = None) -> Tuple[int, List[int]]:
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            counts = [0] * len(words)
            total_words = 0
            unique_words = set()
            for page in pdf_reader.pages:
                text = page.extract_text().lower()
                total_words += len(text.split())
                unique_words.update(text.split())
                for i, word in enumerate(words):
                    counts[i] += text.count(word.lower())
            if output_file:
                output_file = "findr.csv"
                with open(output_file, 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(["Word", "Count"])
                    for i, word in enumerate(words):
                        writer.writerow([word, counts[i]])
            return total_words, len(unique_words), counts
    except FileNotFoundError as e:
        print("File not found:", e)
        return -1, []
    except PyPDF2.utils.PdfReadError as e:
        print("Error reading PDF file:", e)
        return -1, []

def input_data():
    pdf_path = input("Enter the path to the pdf file: ")
    words = input("Enter the word(s) to search for separated by commas: ").strip().split(',')
    return pdf_path, words

pdf_path, words = input_data()
total_words, unique_words, counts = findr(pdf_path, words)
if total_words != -1:
    print(f'The pdf contains {total_words} total words and {unique_words} unique words')
    print(f'Results have been written to findr.csv')
else:
    print("An error occured")
