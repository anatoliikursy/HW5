def word_count(text):  #-- рахує кількість слів в тексті          
    words = text.split()
    return len(words)

def character_count(text): # -- рахує кількість символів у тексті
    return len(text)

def unique_words(text): #-- повертає кількість унікальних слів
    words = text.split()
    count_unique = len(set(words))
    return (count_unique)