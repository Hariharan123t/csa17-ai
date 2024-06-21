from collections import deque

# Define the grid
# 0 represents a clean cell, 1 represents a dirty cell
grid = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Define the starting position of the vacuum cleaner
start_position = (0, 0)

# Directions the vacuum can move: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid_position(grid, position):
    rows, cols = len(grid), len(grid[0])
    x, y = position
    return 0 <= x < rows and 0 <= y < cols

def bfs_clean(grid, start_position):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start_position, [])])
    visited = set()
    
    while queue:
        (x, y), path = queue.popleft()
        
        # If the current cell is dirty, clean it
        if grid[x][y] == 1:
            grid[x][y] = 0
        
        # Check if all cells are clean
        if all(grid[i][j] == 0 for i in range(rows) for j in range(cols)):
            return path + [(x, y)]
        
        # Explore adjacent cells
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_position(grid, (new_x, new_y)) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append(((new_x, new_y), path + [(x, y)]))
    
    return None

solution = bfs_clean(grid, start_position)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
