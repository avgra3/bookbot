import sys
import logging
from stats import num_of_words, character_count


def main() -> None:
    usageMessage = "Usage: python3 main.py <path_to_book>"
    if len(sys.argv) > 2:
        logging.error("You can supply no more than 1 book.")
        logging.info(usageMessage)
        print(usageMessage)
        sys.exit(1)

    if len(sys.argv) < 2:
        logging.error("You need to supply 1 book.")
        logging.info(usageMessage)
        print(usageMessage)
        sys.exit(1)

    raw_book_path = sys.argv[1]
    with open(raw_book_path) as f:
        book = f.read().lower()

    report_intro = f"--- Begin report of {raw_book_path} ---"
    print(report_intro)
    word_count = num_of_words(book)
    print(f"{word_count} words found in the document\n\n")
    count_of_chars = character_count(book)
    for char, count in count_of_chars.items():
        print(f"{char}: {count}")
    print("--- End report ---")


if __name__ == "__main__":
    main()
