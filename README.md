# **Findr** #

This program allows you to count the number of occurrences of a word in a PDF file. It takes in the path to a PDF file, a list of words to search for, and an optional output file path as input. The program then counts the number of occurrences of each word in the PDF, and returns the total number of words and unique words in the PDF. If an output file path is provided, the program will write the results to a CSV file named 'findr.csv' in the current directory

## Requirements
Python 3.x
PyPDF2 library
csv library

## **Usage
Clone the repository or download the script.
Open a terminal and navigate to the directory where the script is located.
Run the script with the command python findr.py
When prompted, enter the path to the PDF file you want to search.
Enter the word(s) you want to search for, separated by commas.
Optionally, enter the path to the output file.
The program will then count the occurrences of each word in the PDF and return the total number of words and unique words in the PDF, and write the results to a CSV file named 'findr.csv' in the current directory if an output file path was provided.

Please note that the program may not work for scanned PDFs. In that case, you would need to use OCR (Optical Character Recognition) to convert the scanned image to text before running this code.

## **Possible Enhancements
Search for multiple words at the same time
Handle cases where the pdf file is not a standard pdf or the pdf is malformed by adding more exception handling
Add functionality to count total number of words in the PDF, or counting the number of unique words in the PDF
Add a command line interface using a library such as argparse to allow the user to pass the pdf path, word to search and output file as command-line arguments
Improve the speed of the program by using other libraries such as pdfminer or slate to extract text and compare the results.

## **Support
In case of any issues or if you have any suggestions for improvements, please open an issue or contact me.

## **Conclusion
This program provides a simple solution for counting the occurrences of specific words in a PDF file. It allows the user to input a PDF file, a list of words to search for, and an optional output file path. It then counts the occurrences of each word in the PDF, returns the total number of words and unique words in the PDF and writes the results to a CSV file if the output file path is provided.