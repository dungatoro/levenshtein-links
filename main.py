import pickle 
from sys import argv

words = pickle.load(open("words.pickle", "rb"))

def shortest_path(a, b):
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

def show_shortest_path(a, b):
    path = shortest_path(a, b)
    if path:
        for i, word in enumerate(path):
            print(f" {i+1}) {word}")
    else:
        print("No path found.")

def find_furthest_node(words):
    stack = [(word, 0)]
    visited = set() 
    max_depth_node = (word, 0)
    while stack:
        node, depth = stack.pop()
        if node not in visited:
            visited.add(node)
            
            if depth > max_depth_node[1]:
                max_depth_node = (node, depth)
            
            for neighbor in words.get(node, []):
                if neighbor not in visited:
                    stack.append((neighbor, depth + 1))
    
    return max_depth_node[0]

def largest_distance():
    # drippy and yammering
    best = "", ""
    best_len = 0
    for i, word in enumerate(words):
        print(len(words)-i)
        furthest = find_furthest_node(words, word)
        path = shortest_path(words, word, furthest)
        if len(path) > best_len:
            best_len = len(path)
            best = word, furthest

show_shortest_path(argv[1], argv[2])
