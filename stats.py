def num_of_words(book: str) -> int:
    words = book.split()
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
    return dict(sorted(char_count.items(), key=lambda x: x[1], reverse=True))
