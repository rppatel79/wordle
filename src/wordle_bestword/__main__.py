from .constants import ANSWER_WORDS_FILE, VALID_WORDS_FILE
from .wordle_start_word_optimizer import read_answer_words, read_valid_words, analyze_word_sets


def main() -> None:
    answers = read_answer_words(ANSWER_WORDS_FILE)
    valid_words = read_valid_words(VALID_WORDS_FILE)
    best_word, best_score = analyze_word_sets(answers, valid_words)
    print(f"Best starting word: {best_word} (score: {best_score})")


if __name__ == "__main__":
    main()