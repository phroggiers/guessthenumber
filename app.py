from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# A simple model for incoming guesses
class Guess(BaseModel):
    number: int

# Store the generated number in memory (for simplicity)
secret_number = random.randint(1, 10)

@app.get("/")
def read_root():
    return {"message": "Welcome to Guess the Number! Send your guess as a POST request to /guess"}

@app.post("/guess")
def make_guess(guess: Guess):
    if guess.number < 1 or guess.number > 10:
        return {"result": "Please guess a number between 1 and 10."}
    
    if guess.number == secret_number:
        return {"result": "Congratulations! You've guessed the number!"}
    else:
        return {"result": "Try again!"}

# To run the application locally, use: uvicorn app:app --reload
