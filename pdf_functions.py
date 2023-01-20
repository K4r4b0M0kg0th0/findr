import PyPDF2
import re
import csv
from typing import Tuple, List

EXACT_MATCH = 'exact'
PARTIAL_MATCH = 'partial'
REGEX_MATCH = 'regex'

def findr(pdf_path: str, words: List[str], output_file: str = None, match_type:str=EXACT_MATCH, return_type:str='tuple') -> Tuple[int, List[int]]:
    """
    This function reads a pdf file and counts the occurrences of specified words in it.
    :param pdf_path: The path to the pdf file
    :param words: List of words to search for
    :param output_file: The path for the output file
    :param match_type: The type of match to use (exact, partial, regex)
    :param return_type: The type of return value (tuple, dict)
    :return: Tuple (total_words, unique_words, counts) or a dictionary containing word count and percentage
    """
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
                    if match_type == EXACT_MATCH:
                        counts[i] += text.count(word.lower())
                   
                    elif match_type == PARTIAL_MATCH:
                        counts[i] += len([w for w in text.split() if word.lower() in w])
                    elif match_type == REGEX_MATCH:
                        counts[i] += len(re.findall(word.lower(), text))
                    else:
                        raise ValueError(f"Invalid match type: {match_type}. match_type must be either 'exact', 'partial' or 'regex'.")
            if output_file:
                with open(output_file, 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(["Word", "Count", "Percentage"])
                    for i, word in enumerate(words):
                        percentage = counts[i]/total_words
                        writer.writerow([word, counts[i], percentage])
            if return_type == 'tuple':
                return total_words, len(unique_words), counts
            elif return_type == 'dict':
                result = {}
                for i, word in enumerate(words):
                    result[word] = {'count':counts[i], 'percentage':counts[i]/total_words}
                return result
            else:
                raise ValueError(f"Invalid return type: {return_type}. return_type must be either 'tuple' or 'dict'.")
    except FileNotFoundError as e:
        print("File not found:", e)
    except PyPDF2.utils.PdfReadError as e:
        print("Error reading PDF file:", e)
    except ValueError as e:
        print(e)
