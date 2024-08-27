import pickle 
from sys import argv

def shortest_path(words, a, b):
    if a == b: return []

    if a not in words:
        print(f'"{a}" is not in the word list.')
        return []
    elif b not in words:
        print(f'"{b}" is not in the word list.')
        return []

    paths = [[a]]
    path_num = 0 
    visited = {a}
        
    while path_num < len(paths):
        current_path = paths[path_num] 
        current_word = current_path[-1] 
        next_words = words[current_word]

        if b in next_words:
            path = current_path+[b]
            return path

        for word in next_words:
            if not word in visited:
                paths.append(current_path+[word]) 
                visited.add(word) 

        path_num += 1
    return []

def show_shortest_path(words, a, b):
    path = shortest_path(words, a, b)
    if path:
        for i, word in enumerate(path):
            print(f" {i+1}) {word}")
    else:
        print("No path found.")

words = pickle.load(open("words.pickle", "rb"))
show_shortest_path(words, argv[1], argv[2])
