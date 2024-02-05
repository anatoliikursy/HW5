import text_processor as pro

input_text = input("Введіть текст: ")

without = pro.remove_punctuation(input_text)
print("Текст без пунктуації:", without)    
    
lower = pro.convert_to_lowercase(input_text)
print("Текст у нижньому регістрі:", lower)
    
text_list = pro.tokenize_text(input_text)
print("Список слів:", text_list)

sentences_list = pro.sentence_tokenize(input_text)
print("Список речень:", sentences_list)
    
words_count = pro.word_count(input_text)
print("Кількість слів: ", words_count)    
    
characters_count = pro.character_count(input_text)
print("Кількість слів: ", characters_count)    

unique = pro.unique_words(input_text)
print("Кількість унікальних слів: ", unique)

average_words_length  = pro.average_word_length(input_text)
print("Cередня довжина слів: ", average_words_length)

unique_word_count = pro.count_unique_words(input_text)
print("Кількість унікальних слів у тексті: ", unique_word_count)

