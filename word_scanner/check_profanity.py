import urllib

def read_txt():
    # Contents only detect profanity words in English
    quotes = open("/Users/$USER/Desktop/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)

    # It is good convention to close any file we have opened in the program.
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()

    # print(output)
    if "true" in output:
        print("There are one or more bad words in the document.")
    elif "false" in output:
        print("This file has no bad words in it.")
    else:
        print("Could not scan the document properly.")

# We call the function to read text in the tt file
read_txt()
