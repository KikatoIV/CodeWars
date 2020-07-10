def is_isogram(word): 
    clean_word = word.lower() 
    letter_list = [] 
    for letter in clean_word: 
        if letter.isalpha(): 
            if letter in letter_list: 
                return False
            letter_list.append(letter)
    return True

print(is_isogram("Algorism"),
is_isogram("PasSword"),
is_isogram("Dermatoglyphics"),
is_isogram("Cat"),
is_isogram("Filmography"),
is_isogram("Consecutive"),
is_isogram("Bankruptcies"),
is_isogram("Unforgivable"),
is_isogram("Unpredictably"),
is_isogram("Moose"))
    