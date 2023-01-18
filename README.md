Python program that uses the PyPDF2 library to read a PDF file and count the number of times a specific word appears in the file

Error handling is added using try-except block, in case the pdf file is not found or is in an invalid format it will print the error message and return -1.
The word and text are converted to lowercase before counting to match words regardless of their capitalization.
A progress indicator is added to the loop to show the progress of the loop, you could use the tqdm library to add a progress bar to the loop.
An additional functionality is added to return -1 in case of an error instead of printing the error message.
The function takes in an additional argument output_file which is an optional argument, if provided the function will write the results to the file.
The function now takes in a list of words to search for and returns a tuple containing total number of words and unique words in the pdf and a list of counts for each word.
The function now also counts total number of words and unique words in the pdf