import PyPDF2

def count_word_in_pdf(pdf_path, word):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        count = 0
        for page in range(pdf_reader.numPages):
            pdf_page = pdf_reader.getPage(page)
            count += pdf_page.extractText().count(word)
    return count

pdf_path = '/home/k4r4bo/Downloads/cv part 2(1).pdf'
word = 'example'
count = count_word_in_pdf(pdf_path, word)
print(f'The word "{word}" appears {count} times in the PDF.')
