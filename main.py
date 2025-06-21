import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

from stats import count_words
from stats import count_chrs
from stats import report

def main():
    #book_path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        book_text = get_book_text(sys.argv[1])
        words = count_words(book_text)
        report(count_chrs(book_text))

main()