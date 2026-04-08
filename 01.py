import random

# List of predefined words
words = ["apple", "tiger", "chair", "plant", "bread"]

# Randomly choose a word
word = random.choice(words)

# Create a display with underscores
display = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Limit incorrect guesses
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")

# Game loop
while incorrect_guesses < max_incorrect and "_" in display:
    print("\nWord:", " ".join(display))
    guess = input("Guess a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is in the word
    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Incorrect guesses:", incorrect_guesses, "/", max_incorrect)

# Game result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)