import re

def longest():
    try:
        with open("zen.txt", "r") as file:
            content = file.read()

        words = re.findall(r"[A-Za-z]+", content)

        if words:
            print("Longest word:", max(words, key=len))
        else:
            print("Error: No words found")

    except OSError as error:
        print("Error:", error)


longest()
