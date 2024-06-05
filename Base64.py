# How the program works:

# Line 1 imports the Base64 Python library.
# Line 3 converts the message to bytes using Unicode (‘utf-8’ stands for Unicode Transformation Format using 8 bits).
# Line 4 carries out the Base64 encoding on the bytes.
# Line 5 converts the bytes back to alphanumeric characters using Unicode.
# Lines 7–21 print the message, the byte representation, the Base64 representation and the encoded output.
# Each line is printed one character at a time.
# Lines 23–29 reverse the process.


import base64
message = "Dog"
message_bytes = message.encode("utf-8")
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode("utf-8")

for char in message:
    print(char, end="  ")
print()

for char in message_bytes:
    print(char, end=" ")
print("\n")

for char in base64_bytes:
    print(char, end="  ")
print()
print(" ", end="")

for char in base64_message:
    print(char, end="  ")

print("\n\nAnd now to decode...")


# encoded message

base64_message = "RG9n"
base64_bytes = base64_message.encode("utf-8")
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode("utf-8")


print(message)
