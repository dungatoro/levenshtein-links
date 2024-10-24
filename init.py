from string import ascii_lowercase as alphabet
import pickle

words = {word.strip(): [] for word in open("words.txt", "r")}

for i, word in enumerate(words):
    if i%1000 == 0:
        print(len(words)-i)

    new_words = []
    for new_letter in alphabet:
        # substitution
        for i in range(len(word)):
            new_words.append(word[:i]+new_letter+word[i+1:])
    
        # insertion
        for i in range(len(word)+1):
            new_words.append(word[:i]+new_letter+word[i:])
    
    # deletion
    for i in range(len(word)):
        new_words.append(word[:i]+word[i+1:])
    
    for new_word in new_words:
        if new_word != word and new_word in words:
            words[word].append(new_word)

pickle.dump(words, open("words.pickle", "wb"))
