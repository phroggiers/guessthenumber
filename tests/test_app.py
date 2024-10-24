from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    # Test the GET request to the root endpoint
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to Guess the Number" in response.text

def test_make_guess_correct():
    # Set the secret number to a known value for testing
    global secret_number
    secret_number = 5  # Mock the secret number for testing

    # Test guessing the correct number
    response = client.post("/guess", json={"number": 5})
    assert response.status_code == 200
    assert response.json() == {"result": "Congratulations! You've guessed the number!"}

def test_make_guess_incorrect():
    # Set the secret number to a known value for testing
    global secret_number
    secret_number = 5  # Mock the secret number for testing

    # Test guessing an incorrect number
    response = client.post("/guess", json={"number": 3})
    assert response.status_code == 200
    assert response.json() == {"result": "Try again!"}

def test_make_guess_out_of_range():
    # Test a guess that is out of range (below 1)
    response = client.post("/guess", json={"number": 0})
    assert response.status_code == 200
    assert response.json() == {"result": "Please guess a number between 1 and 10."}

    # Test a guess that is out of range (above 10)
    response = client.post("/guess", json={"number": 11})
    assert response.status_code == 200
    assert response.json() == {"result": "Please guess a number between 1 and 10."}
