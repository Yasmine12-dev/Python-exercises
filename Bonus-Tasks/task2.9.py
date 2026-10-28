import re
from collections import Counter

def word_frequency():
    try:
        with open("zen.txt", "r") as file:
            content = file.read().lower()

        words = re.findall(r"[a-z]+", content)

        counts = Counter(words)

        for word, count in sorted(counts.items()):
            print(word, ":", count)

    except OSError as error:
        print("Error:", error)


word_frequency()
