# app.py
import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    number_to_guess = random.randint(1, 10)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1
            if guess < 1 or guess > 10:
                print("Please enter a number within the range.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()
