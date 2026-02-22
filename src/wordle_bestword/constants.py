from pathlib import Path

# constants.py lives at: <project_root>/src/wordle_bestword/constants.py
# project root is two levels up from /src/wordle_bestword -> /src -> <root>
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data directory
DATA_DIR = PROJECT_ROOT / "data"

# Input files
ANSWER_WORDS_FILE = DATA_DIR / "wordle.txt"
VALID_WORDS_FILE = DATA_DIR / "valid_five_letter_words.txt"