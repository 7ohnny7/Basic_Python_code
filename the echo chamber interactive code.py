"""pointless interactive loop - this program will keep asking for input until
the user enters 'quit'"""
exit = False
print('Type quit to end program')
while not exit:
    user_input = input('what is your name: ')
    if user_input == 'quit':
        exit = True
    else:
        print(user_input)


