def palindrome(word):
    if len(word) <= 1:
        return True

    if word[0] != word[-1]:
        return False

    return palindrome(word[1:-1])


text = input("Enter a sentence: ")

cleaned = ""

for letter in text.lower():
    if letter.isalnum():
        cleaned += letter

print(palindrome(cleaned))
