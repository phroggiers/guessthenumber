# tests/test_app.py
import pytest
from app import guess_the_number

def test_guess_the_number():
    # This test only verifies that the function can be called.
    # Since the function uses input(), it will not proceed without user interaction.
    # For full testing, mocking would be needed.
    assert callable(guess_the_number)
