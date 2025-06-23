from stats import get_num_words, get_char_counts, sort_dict
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

try: 
    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(book))} total words")
    print("--------- Character Count -------")
    sorted_list = sort_dict(get_char_counts(get_book_text(book)))
    for char in sorted_list:
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)