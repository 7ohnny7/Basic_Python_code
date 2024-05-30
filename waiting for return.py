# A docstring for the flashcard program"""
"""
This flashcard program allows the user to ask for a glossary entry.
In response, the program randomly picks an entry from all glossary entries. It shows the entry.
After the user presses return, the program shows the definition of that particular entry.
The user can repeatedly ask for an entry and also
has the option to quit the program
"""

from random import *

user_input = input('press return to see the definition: ')

# show a flash card
glossary = {'word1': 'definition1', 'word2': 'definition2', 'word3': 'definition3'}
    
        
