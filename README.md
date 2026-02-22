# Wordle Best Starting Word Optimizer

This project analyzes historical Wordle answers and a list of valid five-letter words to determine the best possible starting word based on letter frequency.

With the included dataset, the current best starting word is:

## 📦 Project Structure
```
wordle_bestword/
├── data/
│ ├── wordle.txt
│ └── valid_five_letter_words.txt
├── src/
│ └── wordle_bestword/
│ ├── main.py
│ ├── constants.py
│ └── wordle_start_word_optimizer.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## 🚀 Clone the Repository

```bash
git clone https://github.com/<your-username>/wordle_bestword.git
cd wordle_bestword
```

## Set Up a Virtual Environment
### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows (Command Prompt)
```bash
python -m venv .venv
.venv\Scripts\activate
```

## Install the Project
Install in editable mode so code changes are picked up automatically:
```bash
pip install -e .
```

## Run the Program
From the project root:
```bash
pip install -e .
```