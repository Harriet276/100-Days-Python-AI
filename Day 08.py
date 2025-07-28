# Day 08: File I/O in Python
from importlib.resources import contents


#Practice Question #1

# Open a .txt file.
# Count the number of words, lines, and characters.
# Print the 5 most common words.

from collections import Counter
import string

def commonwordsinafile():
    with open('Movies&Showstowatch .txt', 'r') as  file:
        contents = file.read()
        contents = contents.translate(str.maketrans('', '', string.punctuation)).lower()
        words = contents.split()
        dictionary = {}
        line_count = contents.count('\n')
        word_count = len(words)
        char_count = len(contents)
        most_common = Counter(words).most_common(5)
        for word, count in most_common:
            print(f"word{word} : {count}")


##Practice Question #2
#Read a file and remove all punctuation from the text.
def textcleaner(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        contents = contents.translate(str.maketrans('','',string.punctuation)).lower()
        print(list(contents))


#Practice Question #3
#Write a program that reads a list of names and writes only the capitalized names to a new file.

def writeonlyCapitalizedNames(names):
    with open("Testing1.txt", 'w') as file:
        for name in names:
             if name and names[0].isupper():
                 file.write(name + '\n')
                

#Practice Question #4
#Append the current timestamp to a log file every time the script runs.
from datetime import datetime
def appendcurrentTime(filename):
        current_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        with open(filename, 'a') as logfile:
            logfile.write(f"Script ran at: {current_time}\n")



commonwordsinafile()