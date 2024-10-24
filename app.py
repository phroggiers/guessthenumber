from fastapi import FastAPI, Request
from pydantic import BaseModel
import random
from fastapi.responses import HTMLResponse

app = FastAPI()

# A simple model for incoming guesses
class Guess(BaseModel):
    number: int

# Store the generated number in memory (for simplicity)
secret_number = random.randint(1, 10)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Guess the Number</title>
        </head>
        <body>
            <h1>Welcome to Guess the Number!</h1>
            <form action="/guess" method="post">
                <label for="number">Enter your guess (1-10):</label>
                <input type="number" id="number" name="number" min="1" max="10" required>
                <button type="submit">Guess</button>
            </form>
        </body>
    </html>
    """

@app.post("/guess", response_class=HTMLResponse)
def make_guess(request: Request, number: int):
    if number < 1 or number > 10:
        return HTMLResponse(content="Please guess a number between 1 and 10.", status_code=200)
    
    if number == secret_number:
        return HTMLResponse(content="Congratulations! You've guessed the number!", status_code=200)
    else:
        return HTMLResponse(content="Try again!", status_code=200)
