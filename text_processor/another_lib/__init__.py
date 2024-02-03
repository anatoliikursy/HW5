import nltk

def sentence_tokenize(text):
    sentences = nltk.sent_tokenize(text)
    return sentences