from collections import Counter

def letter_frequency():
    try:
        with open("zen.txt", "r") as file:
            content = file.read().lower()

        letters = [char for char in content if char.isalpha()]

        counts = Counter(letters)

        for letter, count in sorted(counts.items()):
            print(letter, ":", count)

    except OSError as error:
        print("Error:", error)


letter_frequency()
