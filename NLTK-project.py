import wikipedia
import codecs
import nltk


# function to read the input file(s)
def read_lines(file):
    with codecs.open(file, "r", "utf-8") as reader:
        return reader.readlines()


# function to extract the required data/information from the Wikipedia articles that accepts text files as arguments
def extract_data(file):
    '''to clear the output file before appending the required data from the chosen Wiki articles to the output file
    (if I have more input files and want to collect the data of all wikipedia articles from different input
    files in one output file, this part of the code can be disabled)'''
    codecs.open("output.txt", "w", "utf-8").close()

    # start a loop to read every line (aka Wiki article) of the text file and perform data extraction
    for line in read_lines(file):
        # try except block to handle the recurring error with the Marie Curie article
        try:
            # get content of wikipedia articles
            page = wikipedia.page(line)

            # split content into words
            words = page.content.split()

            # get word count
            word_count = len(words)

            # get number of links
            link_count = len(page.links)

            # pos tag the words and get all pronouns (PRP and PRP$)
            pos = nltk.pos_tag(words)
            prp_count = 0
            for e in pos:
                if e[1] == "PRP" or e[1] == "PRP$":
                    prp_count += 1

            # get all male personal pronouns (subjective, objective, reflexive, possessive)
            male_count = 0
            for e in pos:
                if e[0].lower() in ["he", "him", "himself", "his"]:
                    male_count += 1

            # get all female personal pronouns (subjective, objective, reflexive, possessive)
            female_count = 0
            for e in pos:
                if e[0].lower() in ["she", "her", "herself", "hers"]:
                    female_count += 1

            # print the required data from every Wikipedia article to an output file
            with codecs.open("output.txt", "a", "utf-8") as text_file:
                print(" "
                      f"Name of the Wikipedia article:      {line.strip()}"+"\n",
                      f"Word count:                         {word_count}"+"\n",
                      f"Number of links:                    {link_count}"+"\n",
                      f"Number of all pronouns:             {prp_count}"+"\n",
                      f"Number of male pronouns:            {male_count}"+"\n",
                      f"Number of female pronouns:          {female_count}"+"\n", file=text_file)
            text_file.close()

        except wikipedia.exceptions.WikipediaException:
            # a message for error handling
            print("An error occurred. One or more articles could not be found. They will be excluded "
                  "from the final result.")


# code to run the program
extract_data("wikipedia_articles.txt")
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
NLTK-project.py[+] [unix] (00:59 01/01/1970)                             1,1 All
-- INSERT --

