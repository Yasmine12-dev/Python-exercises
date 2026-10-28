message = input("Enter the encrypted message: ")
key = int(input("Enter the key (1-25): "))

decrypted = ""

for letter in message:
    if letter.isalpha():
        if letter.islower():
            start = ord("a")
        else:
            start = ord("A")

        new_letter = chr((ord(letter) - start - key) % 26 + start)
        decrypted += new_letter
    else:
        decrypted += letter

print("Decrypted message:", decrypted)
