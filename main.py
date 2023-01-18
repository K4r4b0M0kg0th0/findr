import os
import PyPDF2
from typing import List, Tuple

def count_word_in_pdf(pdf_path: str, words: List[str], output_file: str = None) -> Tuple[int, List[int]]:
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
                with open(output_file, 'w') as f:
                    for i, word in enumerate(words):
                        f.write(f'{word} appears {counts[i]} times in the PDF.\n')
            return total_words, len(unique_words), counts
    except FileNotFoundError as e:
        print("File not found:", e)
        return -1, []
    except PyPDF2.utils.PdfReadError as e:
        print("Error reading PDF file:", e)
        return -1, []

pdf_path = 'path/to/pdf/file.pdf'
words = ['example', 'word']
output_file = 'counts.txt'
total_words, unique_words, counts = count_word_in_pdf(pdf_path, words, output_file)
if total_words != -1:
    print(f'The pdf contains {total_words} total words and {unique_words} unique words')
    for i, word in enumerate(words):
        print(f'The word "{word}" appears {counts[i]} times in the PDF.')
else:
    print("An error occured")
