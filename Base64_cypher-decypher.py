import base64
message = "Dog"
message_bytes = message.encode("utf-8")
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode("utf-8")

for char in message:
    print(char, end = "     ")
print()

for char in message_bytes:
    print((char), end = "   ")
print("\n")

for char in base64_bytes:
    print((char), end = "   ")
print()
print(" ", end ="")

for char in base64_message:
    print((char), end = "    ")

print("\n\nAnd now to decode...")

base64_message = "RG9n" #encoded message
base64_bytes = base64_message.encode("utf-8")
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode("utf-8")
print(message)
