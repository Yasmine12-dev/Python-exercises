words = ["apple", "banana", "kiwi", "pear"]

i = 0

while i < len(words):
    if len(words[i]) > 4:
        words.pop(i)
    else:
        i += 1

print(words)
