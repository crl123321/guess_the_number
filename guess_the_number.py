import random
import art

to_guess = random.randint(1,100)

difficulty = {
    "easy": 10,
    "hard": 5,
}

def guesser(tries):
    print(f"You have {tries} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    return guess

def checker(user_guess, life_points):
    if user_guess == to_guess:
        return life_points * -1
    else:
        if user_guess < to_guess:
            print("Too low.")
        else:
            print("Too high.")
        return life_points - 1
    
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

lives = difficulty[level]
while lives != 0:
    number = guesser(lives)
    lives = checker(number, lives)
    if lives == 0:
        print("You've ran out of guesses. Refresh the page to play again.")
    elif lives < 0:
        lives = 0
        print(f"You got it! The answer was {to_guess}.")
    else:
        print("Guess again.")