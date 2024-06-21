def dfs(graph, start):
    # Use a stack for DFS
    stack = [start]
    # Keep track of visited nodes
    visited = set()
    # To store the order of traversal
    order = []

    while stack:
        # Pop a node from the stack
        node = stack.pop()
        if node not in visited:
            # Mark the node as visited
            visited.add(node)
            order.append(node)
            # Push all adjacent nodes (neighbors) to the stack
            for neighbor in reversed(graph[node]):  # Reverse to maintain order consistency
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return order

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    start_node = 'A'
    dfs_order = dfs(graph, start_node)
    print("DFS traversal order:", dfs_order)
