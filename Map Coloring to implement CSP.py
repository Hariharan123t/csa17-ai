class MapColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.solution = {}
    
    def is_valid(self, node, color):
        for neighbor in self.graph[node]:
            if neighbor in self.solution and self.solution[neighbor] == color:
                return False
        return True
    
    def solve(self):
        return self.backtrack()
    
    def backtrack(self):
        if len(self.solution) == len(self.graph):
            return True
        
        node = self.select_unassigned_variable()
        
        for color in self.colors:
            if self.is_valid(node, color):
                self.solution[node] = color
                if self.backtrack():
                    return True
                del self.solution[node]
        
        return False
    
    def select_unassigned_variable(self):
        for node in self.graph:
            if node not in self.solution:
                return node
        return None

# Example usage
if __name__ == "__main__":
    # Example graph (map) represented as an adjacency list
    graph = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW']
    }
    
    # List of available colors
    colors = ['Red', 'Green', 'Blue']
    
    # Create MapColoring object
    map_coloring = MapColoring(graph, colors)
    
    # Solve the problem
    if map_coloring.solve():
        print("Solution found:")
        for node, color in map_coloring.solution.items():
            print(f"{node}: {color}")
    else:
        print("No solution found.")
