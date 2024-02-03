def remove_punctuation(text):  #-- повертає на виході текст без знаків пунктуації
    punctuation_symbols = '!()-[];:",<>./?@#$%^&*_~'
    text_without_punt = ''.join(symbol for symbol in text if symbol not in punctuation_symbols)
    return text_without_punt

def convert_to_lowercase(text):    #-- переводить текст у нижній регістр
    lowercase_text = text.lower()
    return lowercase_text

def tokenize_text(text):  #-- переводить текст у список слів          
    words = text.split()
    return words






# average_word_length(text) -- рахує середню довжину слів у тексті
# find_occurrences(text, keyword) -- рахує кількість разів появи слова у тексті