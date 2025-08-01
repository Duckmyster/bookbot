from stats import get_word_count
from stats import char_count

def get_book_text(filepath):
    with open(filepath) as text:
        text_contents = text.read()
        return text_contents
#converts filepath to string



def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")
    print(char_count(text))

main()