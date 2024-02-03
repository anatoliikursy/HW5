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
    
    
    
    
    
