# test the program using the python shell"""
"""
This flashcard program allows the user to ask for a glossary entry.
In response, the program randomly picks an entry from all glossary entries. It shows the entry.
After the user presses return, the program shows the definition of that particular entry.
The user can repeatedly ask for an entry and also
has the option to quit the program
"""
from random import *

def show_flashcard():
    """show the user a random key and ask them to define it
- show the definition when the user presses return."""
    random_key = choice(list(glossary))
    print('define: ', random_key)
    input('press return to see the definition: ')
    print(glossary[random_key])

# show a flashcard

glossary = {'word1': 'definition1', 'word2': 'definition2', 'word3': 'definition3'}

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
       
       
