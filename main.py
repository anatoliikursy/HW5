import text_processor as pro

text_without = input("Введіть текст: ")
without = pro.remove_punctuation(text_without)
print(without)
    
text_lower = input("Введіть текст: ")
lower = pro.convert_to_lowercase(text_lower)
print(lower)
    
text_into_list = input("Введіть текст: ")   
text_list = pro.tokenize_text(text_into_list)
print(text_list)
    
    
    
    
    
