# Flashcards_for_TM112_GLossary.py
"""
This flashcard program allows the user to ask for a glossary entry.
In response, the program randomly picks an entry from the TM112 glossary file.
After the user presses return, the program shows the definition of that particular entry.
The user can repeatedly ask for an entry and also
has the option to quit the program"""

from random import *

import csv

# show a flashcard

def show_flashcard():
    """show the user a random key and ask them to define it
- show the definition when the user presses return."""
    random_key = choice(list(glossary))
    print('define: ', random_key)
    input('press return to see the definition: ')
    print(glossary[random_key])

# setup the glossary

def file_to_dictionary(TM112_Glossary):
    """ Return a dictionary with the contents of a file
    """
    file = open(TM112_Glossary, 'r')
    reader = csv.reader(file)
    dictionary = {}
    for row in reader:
        dictionary[row[0]] = row[1]
    return dictionary

glossary = file_to_dictionary('TM112_Glossary.txt')

# The interactive loop
    
exit = False
while not exit:
    user_input = input('press s to show a flashcard or press q to quit ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()    
    else:
        print('You need to enter s or q')
       
