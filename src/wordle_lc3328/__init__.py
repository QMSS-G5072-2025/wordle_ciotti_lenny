# read version from installed package
#from importlib.metadata import version
#__version__ = version("wordle_lc3328")
from .wordle_lc3328 import (
    validate_guess,
    check_guess,
    is_valid_word,
    calculate_game_score,
)

__all__ = [
    "validate_guess",
    "check_guess",
    "is_valid_word",
    "calculate_game_score",
]