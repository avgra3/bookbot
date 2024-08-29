def main() -> None:
    with open("books/frankenstein.txt") as f:
        frankenstein = f.read()
    
    report_intro = "--- Begin report of books/frankenstein.txt ---"
    print(report_intro)
    word_count = num_of_words(frankenstein)
    print(f"{word_count} words fount in the document\n\n")
    count_of_chars = character_count(frankenstein)
    for char, count in count_of_chars.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def num_of_words(book: str) -> int:
    words = book.split(" ")
    count = len(words)
    return count

def character_count(book: str) -> dict[str, int]:
    char_count = {} 
    for char in book.lower():
        if char.isalpha():
            if char in char_count:
             char_count[char] += 1
            else:
                char_count[char] = 1
    return dict(sorted(char_count.items(), key=lambda x:x[1], reverse=True))


if __name__ == "__main__":
    main()
