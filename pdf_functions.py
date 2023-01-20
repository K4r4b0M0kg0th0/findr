import PyPDF2
import re
from typing import Tuple, List

def findr(pdf_path: str, words: List[str], output_file: str = None, match_type:str='exact') -> Tuple[int, List[int]]:
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
                    if match_type == 'exact':
                        counts[i] += text.count(word.lower())
                    elif match_type == 'partial':
                        counts[i] += len([w for w in text.split() if word.lower() in w])
                    elif match_type == 'regex':
                        counts[i] += len(re.findall(word.lower(), text))
                    else:
                        raise ValueError("match_type must be either 'exact', 'partial' or 'regex'.")
            if output_file:
                with open(output_file, 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(["Word", "Count", "Percentage"])
                    for i, word in enumerate(words):
                        percentage = counts[i]/total_words
                        writer.writerow([word, counts[i], percentage])
            return total_words, len(unique_words), counts
    except FileNotFoundError as e:
        print("File not found:", e)
        return -1, []
    except PyPDF2.utils.PdfReadError as e:
        print("Error reading PDF file:", e)
        return -1, []
