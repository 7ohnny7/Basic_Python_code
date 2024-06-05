# Robot Barista program

# Greet customer and ask name.
name = input("Hello!, I am the Robot Barista...\nWhat is you name? :")
print("hi", name)

# Take customer order.
order = input("What can i get for you today? :")

# Hot drink menu
if order == "coffee":
    price = 4.99
elif order == "latte":
    price = 6.99
elif order == "cappuccino":
    price = 7.49
elif order == "americano":
    price = 6.49

# Baristas reponse to order not on menu and program stops.
else:
    print("Sorry, but we do not sell", order)
    price = 0
    exit()

# if item of menu ordered
print("Thank you...\nthat will be","£", price, "\nComing right up!")

# delay response between paying and recieving hot drink
import time
time.sleep(4)

# Complete customer order.
print("Here is your", order, name, "\nHave a nice day!.")

