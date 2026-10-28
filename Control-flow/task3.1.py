message = input("Enter your message: ")
key = int(input("Enter a key (1-25): "))

encrypted = ""

for letter in message:
    if letter.isalpha():
        if letter.islower():
            start = ord("a")
        else:
            start = ord("A")

        new_letter = chr((ord(letter) - start + key) % 26 + start)
        encrypted += new_letter
    else:
        encrypted += letter

print("Encrypted message:", encrypted)
