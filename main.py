import sys

from stats import count_words, open_book

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    file_path = sys.argv[1]
    book = open_book(file_path)
    count_words(book)
