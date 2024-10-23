import pytest
import requests
import os

# Set the SECRET_NUMBER environment variable for testing
os.environ['SECRET_NUMBER'] = '5'

def test_guess_correct():
    response = requests.get("http://localhost:8000/guess?number=5")
    assert response.status_code == 200
    assert response.json()['message'] == "Congratulations! You guessed the number!"

def test_guess_wrong():
    response = requests.get("http://localhost:8000/guess?number=3")
    assert response.status_code == 200
    assert response.json()['message'] == "Wrong guess! The secret number was 5."

def test_guess_out_of_bounds():
    response = requests.get("http://localhost:8000/guess?number=15")
    assert response.status_code == 400  # Expect a bad request for out-of-bounds guess
