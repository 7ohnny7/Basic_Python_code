"""pointless interactive loop - this program will keep asking for input until
the user enters 'quit'"""
exit = False
print('type quit or stop, to end the program')
while not exit:
    user_input = input('How shall i greet you?: ')
    if user_input == 'quit' or user_input == 'stop':
        exit = True
    else:
        print(user_input)


