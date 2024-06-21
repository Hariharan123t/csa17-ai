from collections import deque

# State is represented as (missionaries_left, cannibals_left, boat_position, missionaries_right, cannibals_right)
# boat_position is 0 if the boat is on the left side, and 1 if the boat is on the right side
initial_state = (3, 3, 0, 0, 0)

# Goal state is when all missionaries and cannibals are on the right side
goal_state = (0, 0, 1, 3, 3)

# Possible moves: (missionaries, cannibals)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def is_valid_state(state):
    ml, cl, boat, mr, cr = state
    # Check for invalid numbers
    if ml < 0 or cl < 0 or mr < 0 or cr < 0:
        return False
    # Check that missionaries are not outnumbered by cannibals on either side
    if (ml > 0 and ml < cl) or (mr > 0 and mr < cr):
        return False
    return True

def get_successors(state):
    successors = []
    ml, cl, boat, mr, cr = state
    if boat == 0:  # Boat is on the left side
        for m, c in moves:
            new_state = (ml - m, cl - c, 1, mr + m, cr + c)
            if is_valid_state(new_state):
                successors.append(new_state)
    else:  # Boat is on the right side
        for m, c in moves:
            new_state = (ml + m, cl + c, 0, mr - m, cr - c)
            if is_valid_state(new_state):
                successors.append(new_state)
    return successors

def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        if state == goal_state:
            return path + [state]
        for successor in get_successors(state):
            queue.append((successor, path + [state]))
    return None

solution = bfs(initial_state, goal_state)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
