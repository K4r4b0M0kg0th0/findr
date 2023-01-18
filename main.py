import os
import PyPDF2

def count_word_in_pdf(pdf_path, word):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            count = 0
            for page in range(len(pdf_reader.pages)):
                pdf_page = pdf_reader.pages[page]
                count += pdf_page.extract_text().lower().count(word.lower())
            return count
    except FileNotFoundError as e:
        print("File not found:", e)
        return -1
    except PyPDF2.utils.PdfReadError as e:
        print("Error reading PDF file:", e)
        return -1

pdf_path = 'path/to/pdf/file.pdf'
word = 'example'
count = count_word_in_pdf(pdf_path, word)
if count != -1:
    print(f'The word "{word}" appears {count} times in the PDF.')
else:
    print("An error occured")
