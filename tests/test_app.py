import pytest
from fastapi.testclient import TestClient
from app import app  # Make sure this matches the name of your main app file

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Guess the Number! Send your guess as a POST request to /guess"}

def test_make_guess_correct():
    response = client.post("/guess", json={"number": 5})  # Replace 5 with the actual secret number for testing
    assert response.status_code == 200
    assert response.json() == {"result": "Try again!"}  # Change this based on the secret number

def test_make_guess_out_of_range():
    response = client.post("/guess", json={"number": 15})
    assert response.status_code == 200
    assert response.json() == {"result": "Please guess a number between 1 and 10."}
