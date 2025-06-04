import sys

from stats import get_word_count
from stats import get_char_counts
from stats import create_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(filepath):
    booktext = get_book_text(filepath)
    wordcount = get_word_count(booktext)
    charcounts = get_char_counts(booktext)
    charlist = create_sorted_list(charcounts)
    print("============ BOOKBOT ============\n"
          f"Analyzing book found at {filepath}...\n"
          "----------- Word Count ----------\n"
          f"Found {wordcount} total words \n")
    for dict in charlist:
        print(f"{dict["char"]}: {dict["num"]}")

if len (sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main(sys.argv[1])