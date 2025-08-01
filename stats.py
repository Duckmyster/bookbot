def  get_word_count(text):
    words = text.split() 
    word_count = len(words)
    return word_count
#counts words from string

def char_count(text):
    letter_count = {}
    text_lower = text.lower()
    for word in text_lower:
        letters = word.split()
        for letter in letters:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count                

def dictionary_sort(dictionary):
    for character in dictionary:
        print(character) 