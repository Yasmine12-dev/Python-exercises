import random
from english_words import get_english_words_set

words = get_english_words_set(["web2"], lower=True)

def random_word():
    return random.choice(list(words))

print(random_word())
