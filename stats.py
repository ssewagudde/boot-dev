def open_book(file_path: str) -> str:
    with open(file_path, "r") as f:
        fi = f.read()

    return fi


def get_num_words(book_string: str) -> int:
    book = book_string.split()
    print(f" {len(book)} words found in the document")
    return len(book)


def count_words(book_string):
    f = []
    for word in book_string.split():
        f.append(list(word))

    f = set([item for sublist in f for item in sublist])

    d = []
    for i in f:
        g = {}
        r = book_string.lower().count(i)
        if i.isalpha():
            g["letter"] = i
            g["value"] = r
            d.append(g)
    d.sort(key=lambda x: x["value"], reverse=True)

    d = [f"{i['letter']}: {i['value']}" for i in d]
    d = "\n".join(d)

    d = f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {get_num_words(book_string)} total words
--------- Character Count -------
{d}
"""

    print(d)
