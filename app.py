# app.py
import random

def guess_the_number(user_guess):
    number_to_guess = random.randint(1, 10)
    if user_guess < 1 or user_guess > 10:
        return "Please enter a number within the range."
    elif user_guess < number_to_guess:
        return "Too low! Try again."
    elif user_guess > number_to_guess:
        return "Too high! Try again."
    else:
        return "Congratulations! You guessed the number!"

# For interactive console use
if __name__ == "__main__":
    print("Welcome to 'Guess the Number'!")
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            result = guess_the_number(guess)
            print(result)
            if result.startswith("Congratulations"):
                break
        except ValueError:
            print("Please enter a valid integer.")
