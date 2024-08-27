# DFS implementation to find the furthest node from the starting node
def dfs(graph, node, visited, depth, max_depth_node):
    # Mark the node as visited
    visited.add(node)
    
    # Check if the current node is at a greater depth than the previously recorded maximum depth
    if depth > max_depth_node[1]:
        max_depth_node[0] = node  # Update the node with the maximum depth
        max_depth_node[1] = depth # Update the maximum depth

    # Recursively visit all the neighbors of the current node
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, depth + 1, max_depth_node)

def find_furthest_node(graph, start_node):
    visited = set()  # To keep track of visited nodes
    max_depth_node = [start_node, 0]  # Initialize the furthest node with the start node and depth 0
    
    # Start DFS from the start_node
    dfs(graph, start_node, visited, 0, max_depth_node)
    
    return max_depth_node[0]

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start_node = 'A'
furthest_node = find_furthest_node(graph, start_node)
print(f"The furthest node from {start_node} is {furthest_node}")

