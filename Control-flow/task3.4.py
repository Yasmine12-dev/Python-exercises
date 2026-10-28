english_frequency = [
    8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0,
    6.1, 7.0, 0.15, 0.77, 4.0, 2.4,
    6.7, 7.5, 1.9, 0.095, 6.0, 6.3,
    9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074
]


def decrypt(message, key):
    result = ""
    position = 0

    for letter in message:
        if letter.isascii() and letter.isalpha():
            start = ord("A") if letter.isupper() else ord("a")
            shift = ord(key[position % len(key)]) - ord("a")

            result += chr((ord(letter) - start - shift) % 26 + start)
            position += 1
        else:
            result += letter

    return result


def find_key(message, key_length):
    letters = [c.lower() for c in message
               if c.isascii() and c.isalpha()]

    key = ""

    for position in range(key_length):
        group = letters[position::key_length]
        best_shift = 0
        best_score = float("inf")

        for shift in range(26):
            decoded = [
                (ord(c) - ord("a") - shift) % 26
                for c in group
            ]

            score = 0

            for i in range(26):
                observed = decoded.count(i)
                expected = len(group) * english_frequency[i] / 100

                if expected > 0:
                    score += (observed - expected) ** 2 / expected

            if score < best_score:
                best_score = score
                best_shift = shift

        key += chr(ord("a") + best_shift)

    return key


message = input("Enter encrypted message: ")
key_length = int(input("Enter key length: "))

if key_length <= 0:
    print("Key length must be positive.")
else:
    key = find_key(message, key_length)

    print("Estimated key:", key)
    print("Decrypted message:", decrypt(message, key))
