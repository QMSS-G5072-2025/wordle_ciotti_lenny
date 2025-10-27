
from wordle_lc3328.wordle_lc3328 import (
    validate_guess,
    check_guess,
    is_valid_word,
)


import pytest
def test_validate_guess():
    assert validate_guess("crane") == True # valid guess
    assert validate_guess("Crane") == False # uppercase letters
    assert validate_guess("cran") == False # too short
    assert validate_guess("cranes") == False    # too long
    assert validate_guess("12345") == False # non-alphabetic characters
    
    print("All tests for validate_guess passed!")



def test_guess_check_basic():
    result = check_guess("crane", "crane") # all correct
    expected = [('c', 'green'), ('r', 'green'), ('a', 'green'), ('n', 'green'), ('e', 'green')]
    assert result == expected #assert that the result is equal to expected
    result = check_guess("crane", "blimp") #all gray
    expected = [('b', 'gray'), ('l', 'gray'), ('i', 'gray'), ('m', 'gray'), ('p', 'gray')]
    assert result == expected #assert that the result is equal to expected
    result = check_guess("crane", "react") #mixed
    expected = [('r', 'yellow'), ('e', 'yellow'), ('a', 'green'), ('c', 'yellow'), ('t', 'gray')]
    assert result == expected #assert that the result is equal to expected
    result = check_guess("apple", "cat") #bad length
    expected = []
    assert result == expected #assert that the result is equal to expected

def test_is_valid_word():
    word_list = ["crane", "apple", "hello", "world", "python",
             "house", "water", "light", "music", "dream"]

    assert is_valid_word("crane", word_list) == True  # valid word
    #assert is_valid_word("Crane", word_list) == False  # case-sensitive
    assert is_valid_word("banana", word_list) == False  # not in list
    print("All tests for is_valid_word passed!")

@pytest.mark.parametrize("secret_word, guess, expected", [
("crane","crane",[('c', 'green'), ('r', 'green'), ('a', 'green'), ('n', 'green'), ('e', 'green')]),
("crane","react",[('r', 'yellow'), ('e', 'yellow'), ('a', 'green'), ('c', 'yellow'), ('t', 'gray')]),
("apple","paper",[('p', 'yellow'), ('a', 'yellow'), ('p', 'green'), ('e', 'yellow'), ('r', 'gray')]),
("blimp","crane",[('c', 'gray'), ('r', 'gray'), ('a', 'gray'), ('n', 'gray'), ('e', 'gray')]),
("blimp","cat",[]),
])
def test_check_guess_comprehensive(secret_word, guess, expected):
    result = check_guess(secret_word, guess)
    assert result == expected
@pytest.fixture
def common_word_list():
 
    return [
        "crane", "apple", "hello", "world", "paper",
        "house", "water", "light", "music", "dream"
    ]

def test_is_valid_word_with_fixture(common_word_list):
    assert is_valid_word("crane", common_word_list) == True
    assert is_valid_word("apple", common_word_list) == True
    assert is_valid_word("ghost", common_word_list) == False
    assert is_valid_word("", common_word_list) == False