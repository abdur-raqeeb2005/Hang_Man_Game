import random

lists = ["implementation","software","developer","system","steel"]
get = random.choice(lists)
guessed_get = ["_"] * len(get)
attempts = 5
wrong_guess = 0
guess_let = []

print("Welcome to Hangman!")

while wrong_guess < attempts and "_" in guessed_get:
    print("\nWord: " + " ".join(guessed_get))
    print(f"Guessed Letters: {', '.join(guess_let)}")
    print(f"Incorrect Guesses Left: {attempts - wrong_guess}")
    
    expect = input("Guess a letter: ").lower()

    if expect in guess_let:
        print("You already guessed that letter!")
        continue

    guess_let.append(expect)

    if expect in get:
        for i in range(len(get)):
            if get[i] == expect:
                guessed_get[i] = expect
    else:
        wrong_guess += 1

if "_" not in guessed_get:
    print("\nCongratulations! You guessed the get word:", get)
else:
    print("\nGame over! The get was:", get)
