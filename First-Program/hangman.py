import random


def choose_word(word_length):
    # Bonus 3: I added the possibility to choose a theme
    theme = input("Choose a theme (fruits or animals): ").lower()

    # Ask again if the user enters an invalid theme
    while theme != "fruits" and theme != "animals":
        print("Please choose fruits or animals.")
        theme = input("Choose a theme (fruits or animals): ").lower()

    if theme == "fruits":
        words = ["apple", "banana", "orange", "mango"]
    else:
        words = ["tiger", "monkey", "rabbit", "horse"]

    # Bonus 2: I added a check to see if the word matches the length suggested by the user
    matching_words = []

    for word in words:
        if len(word) == word_length:
            matching_words.append(word)

    # Choose a random word and convert it to uppercase
    return random.choice(matching_words).upper()


def display_word(secret_word, guessed_letters):
    # Display guessed letters and hide the others
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()


def play_game():
    # Bonus 2: I let the user choose the word length
    word_length = int(input("Choose a word length (5 or 6): "))

    while word_length != 5 and word_length != 6:
        print("Please choose 5 or 6.")
        word_length = int(input("Choose a word length (5 or 6): "))

    secret_word = choose_word(word_length)
    guessed_letters = []
    penalties = 0

    # Bonus 1: I let the user choose the maximum penalties
    max_penalties = int(input("Choose the maximum penalties (e.g. 12): "))

    while max_penalties < 0:
        print("Please enter zero or a positive number.")
        max_penalties = int(input("Choose the maximum penalties: "))

    print("Welcome to Hangman!")

    # Keep playing while the penalty limit is not exceeded
    while penalties <= max_penalties:
        display_word(secret_word, guessed_letters)
        print("Penalties:", penalties, "/", max_penalties)

        guess = input("Guess a letter or word: ").strip().upper()

        # Check if the user entered only letters
        if not guess.isalpha():
            print("Please enter letters only!")
            continue

        # If the user guesses one letter
        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed this letter!")
                continue

            guessed_letters.append(guess)

            if guess in secret_word:
                print("Correct letter!")
            else:
                print("Wrong letter!")
                penalties += 1

        # If the user guesses a complete word
        else:
            if guess == secret_word:
                print("You win! The word was", secret_word)
                return
            else:
                print("Wrong word!")
                penalties += 5

        # Check if all letters have been guessed
        won = True

        for letter in secret_word:
            if letter not in guessed_letters:
                won = False

        if won:
            print("You win! The word was", secret_word)
            return

    # The player loses if penalties exceed the limit
    print("You lose! The word was", secret_word)


# Start the game
play_game()
