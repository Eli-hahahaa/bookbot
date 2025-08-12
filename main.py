import sys
from stats import count_words, count_chars, sort_chars_by_freq

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # stats
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = count_words(text)
    raw_freq = count_chars(text)
    freqs = sort_chars_by_freq(raw_freq)

    # report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for d in freqs:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")

    print("============= END ===============")

main()
