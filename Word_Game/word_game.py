import random

# List of secret words
words = ['apple', 'banana', 'orange', 'grape', 'peach']

# Choose one randomly
secret_word = random.choice(words)

print("🎯 Welcome to the Word Guessing Game!")
print("Guess the secret word from this list:")
print(", ".join(words))

attempts = 0

while True:
    guess = input("👉 Enter your guess: ").lower()
    attempts += 1

    if guess == secret_word:
        print(f"🎉 Correct! The word was '{secret_word}'. You guessed it in {attempts} attempts.")
        break
    else:
        print("❌ Wrong guess. Try again!")
