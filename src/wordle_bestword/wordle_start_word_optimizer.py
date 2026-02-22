from collections import Counter
from typing import List, Tuple


def read_word_list(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        return [line.strip().lower() for line in f if line.strip()]


def read_answer_words(file_path: str) -> List[str]:
    return read_word_list(file_path)


def read_valid_words(file_path: str) -> List[str]:
    return read_word_list(file_path)


def build_letter_frequency(words: List[str]) -> Counter:
    freq = Counter()
    for word in words:
        freq.update(word)
    return freq


def score_word(word: str, letter_freq: Counter) -> int:
    return sum(letter_freq[letter] for letter in set(word))


def analyze_word_sets(answer_words: List[str], valid_words: List[str]) -> Tuple[str, int]:
    letter_freq = build_letter_frequency(answer_words)

    best_word = ""
    best_score = -1

    for word in valid_words:
        score = score_word(word, letter_freq)
        if score > best_score:
            best_word = word
            best_score = score

    return best_word, best_score
