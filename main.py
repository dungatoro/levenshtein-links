import pickle 
from sys import argv
from collections import deque, defaultdict

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
        print(f'The shortest path from "{a}" to "{b}":')
        for i, word in enumerate(path):
            print(f" {i+1}) {word}")
    else:
        print("No path found.")

def show_neighbours(word):
    if word in words:
        if words[word]:
            print(f'Words linked to "{word}":')
            for w in words[word]:
                print(f" - {w}")
        else:
            print(f'No words link to "{word}". It is all alone :(')
    else:
        print(f'"{word}" is not in the word list.')

def furthest_word(start_node):
    # Dictionary to track the distance from the start_node to all other nodes
    distances = defaultdict(lambda: float('inf'))
    
    # Queue for BFS
    queue = deque([start_node])
    distances[start_node] = 0
    
    while queue:
        current_node = queue.popleft()
        
        for neighbor in words[current_node]:
            # If the neighbor hasn't been visited, calculate its distance and add it to the queue
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)
    
    # Find the node with the maximum distance
    furthest_node = max(distances, key=distances.get)
    max_distance = distances[furthest_node]
    
    return furthest_node, max_distance

def show_furthest_word(word):
    if word:
        furthest, _ = furthest_word(word)
        print(f'The furthest word from "{word}" is "{furthest}".')
        show_shortest_path(word, furthest)

if len(argv) == 2:
    show_neighbours(argv[1])
elif len(argv) == 3:
    if argv[2] == "--longest":
        show_furthest_word(argv[1])
    else:
        show_shortest_path(argv[1], argv[2])

