import sys
from stats import get_num_words
from stats import count_characters
from stats import convert_and_sort_chars
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_text(sys.argv[1])
    num_words = get_num_words(book_content)
    char_counts = count_characters(book_content)
    sorted_chars = convert_and_sort_chars(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_data in sorted_chars:
        if char_data["char"].isalpha():
            print(f"{char_data['char']}: {char_data['num']}")
    print("============= END ===============")
main()