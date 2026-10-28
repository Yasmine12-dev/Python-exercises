message = input("Enter your message: ")
key = input("Enter your key: ").lower()
choice = input("Encrypt or decrypt (e/d): ")

result = ""
j = 0

for letter in message:
    if letter.isalpha():
        if letter.islower():
            start = ord("a")
        else:
            start = ord("A")

        shift = ord(key[j % len(key)]) - ord("a")

        if choice == "d":
            shift = -shift

        new_letter = chr((ord(letter) - start + shift) % 26 + start)
        result += new_letter
        j += 1

    else:
        result += letter

print("Result:", result)
