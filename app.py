from flask import Flask, request, jsonify
import random
import os

app = Flask(__name__)

# Set a fixed secret number for CI testing purposes
SECRET_NUMBER = os.environ.get('SECRET_NUMBER', random.randint(1, 10))

@app.route('/')
def home():
    return "Welcome to 'Guess the Number'! Use /guess?number=<your_guess> to make a guess."

@app.route('/guess', methods=['GET'])
def guess():
    user_guess = request.args.get('number', type=int)
    
    if user_guess is None:
        return "Please provide a number to guess.", 400
    
    if user_guess < 1 or user_guess > 10:
        return "Guess must be between 1 and 10.", 400
    
    if user_guess == SECRET_NUMBER:
        return jsonify(message="Congratulations! You guessed the number!"), 200
    else:
        return jsonify(message=f"Wrong guess! The secret number was {SECRET_NUMBER}."), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
