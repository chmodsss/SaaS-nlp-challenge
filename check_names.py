from nltk.corpus import names

with open('corncob_lowercase.txt') as f:
    english_words = f.read().splitlines()
    
english_names = [w.lower() for w in names.words()]
non_names = list(set(english_words) - set(english_names))

def check_name(word_in):
    isname = True
    if word_in.istitle():
        for w in word_in.split():
            if w.lower() in non_names:
                isname = False
    return isname