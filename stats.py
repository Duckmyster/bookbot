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
#counts total letters from list of strings           

def dictionary_sort(dictionary):
    def sort_on(item):
        return item["num"]
    #defines what part to sort by within each dictionary in the list
    
    char_dict_list = []
    for character in dictionary:
        char_dict = {
            "char": character, 
            "num": dictionary[character]}
        char_dict_list.append(char_dict)

    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list