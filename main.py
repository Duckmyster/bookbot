import sys
from stats import get_word_count
from stats import char_count
from stats import dictionary_sort



def get_book_text(filepath):
    with open(filepath) as text:
        text_contents = text.read()
        return text_contents
#converts filepath to string



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = get_word_count(text)
    character_count = char_count(text)
    sorted_dictionary = dictionary_sort(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_dictionary:
        if str.isalpha(item["char"]):
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()