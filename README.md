Error handling is added using try-except block, in case the pdf file is not found or is in an invalid format it will print the error message and return -1.
The word and text are converted to lowercase before counting to match words regardless of their capitalization.
A progress indicator is added to the loop to show the progress of the loop, you could use the tqdm library to add a progress bar to the loop.
An additional functionality is added to return -1 in case of an error instead of printing the error message.