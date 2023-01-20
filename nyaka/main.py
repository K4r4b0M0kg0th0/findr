from pdf_functions import nyaka, EXACT_MATCH, PARTIAL_MATCH, REGEX_MATCH
import input_validation

def main():
    pdf_path, words, output_file, match_type, return_type = input_validation.validate_input()
    try:
        result = nyaka(pdf_path, words, output_file, match_type, return_type)
        if isinstance(result, tuple):
            total_words, unique_words, counts = result
            print(f'The pdf contains {total_words} total words and {unique_words} unique words')
            if output_file:
                print(f'Results have been written to {output_file}')
        else:
            print(result)
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
