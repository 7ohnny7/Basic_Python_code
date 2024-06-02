#ROT13 or Caesar Code with a key of 13

plain_Text = input("Enter your secret message: ")
plain_Text = plain_Text.upper()
c_text = ""
for ch in plain_Text:
    code = ord(ch)- ord('A')
    c_code = (code +13) % 26
    c_text = c_text + chr(c_code+65)
print("\nThe encrypted message is: ", c_text)
