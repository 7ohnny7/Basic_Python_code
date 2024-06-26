# Flashcards_for_TM112_Glossary.py
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


# set up the glossary

def file_to_dictionary(tm112_glossary):
    """ Return a dictionary with the contents of a file
    """
    file = open(tm112_glossary, 'r')
    reader = csv.reader(file)
    dictionary = {}
    for row in reader:
        dictionary[row[0]] = row[1]
    return dictionary


glossary = file_to_dictionary('tm112_glossary.txt')

# Engage with user in an interactive loop in which the user can choose
# between being shown a flashcard or quitting

definitions = 0
flashcards = 0


finished = False
while not finished:
    user_input = input('Enter s to show a flashcard or q to quit: ')
    if user_input == 'q':
        finished = True
        print('well done! You managed to get', definitions, 'out of the', flashcards, 'definitions shown correct!')

# Show a random flashcard entry from the glossary        
    elif user_input == 's':
        flashcards = flashcards + 1
        show_flashcard()

# Engage with user in an interactive loop in which the user can choose
# between entering yes or no.

        user_input = input('Did you know the definition? Enter y or n :')
        if user_input == 'y':
            definitions = definitions + 1
    else:
        print('You need to enter either q or s.') 
       
