"""pointless interactive loop - this program will keep asking for input until
the user enters 'quit'"""
exit = False
while exit == False:
    user_input = input('How shall I greet you? ')
    if user_input == 'quit':
        exit = True

    
