def scrabble_score(word):
    scores = {
        "AEIOULNSTR": 1,
        "DG": 2,
        "BCMP": 3,
        "FHVWY": 4,
        "K": 5,
        "JX": 8,
        "QZ": 10
    }

    total = 0

    for letter in word.upper():
        for letters, points in scores.items():
            if letter in letters:
                total += points
                break

    return total


word = input("Enter a word: ")

print("Scrabble score:", scrabble_score(word))
