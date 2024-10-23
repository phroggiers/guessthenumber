# tests/test_app.py
import pytest
from unittest.mock import patch
from app import guess_the_number

def test_guess_the_number_with_mocked_input():
    # Mock input for the test case
    with patch('builtins.input', side_effect=[5]):  # Simulate user input of '5'
        result = guess_the_number(5)
        assert result in [
            "Too low! Try again.",
            "Too high! Try again.",
            "Congratulations! You guessed the number!"
        ]
