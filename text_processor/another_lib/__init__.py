import nltk

def sentence_tokenize(text): #-- переводить текст у список речень
    sentences = nltk.sent_tokenize(text)
    return sentences