def word_count(text):  #-- рахує кількість слів в тексті          
    words = text.split()
    return len(words)

def character_count(text): # -- рахує кількість символів у тексті
    return len(text)

def unique_words(text): #-- повертає кількість унікальних слів
    words = text.split()
    count_unique = len(set(words))
    return (count_unique)

def average_word_length(text): # рахує середню довжину слів у тексті
    
    punctuation_symbols = ' !()-[];:",<>./?@#$%^&*_~'
    text_without_punt = ''.join(symbol for symbol in text if symbol not in punctuation_symbols)
    aver_symb = len(text_without_punt)

    words = text.split()
    aver = int(len(words))
    
    average_length = aver_symb/aver
    return average_length

def count_unique_words(text):  #-- повертає кількість унікальних слів у тексті
    punctuation_symbols = ' !()-[];:",<>./?@#$%^&*_~'
    words = [word.strip(punctuation_symbols) for word in text.split()]
    unique_words = set(words)
    count_unique = len(unique_words)
    return count_unique




# find_occurrences(text, keyword) -- рахує кількість разів появи слова у тексті