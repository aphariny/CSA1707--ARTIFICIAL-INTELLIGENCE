from heapq import heappush, heappop
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_index = GOAL.index(state[i])

            row1 = i // 3
            col1 = i % 3

            row2 = goal_index // 3
            col2 = goal_index % 3

            distance += abs(row1 - row2) + abs(col1 - col2)

    return distance
def get_neighbors(state):
    neighbors = []

    zero_index = state.index(0)

    row = zero_index // 3
    col = zero_index % 3

    moves = [
        (-1, 0),   
        (1, 0),    
        (0, -1),   
        (0, 1)     
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_index = new_row * 3 + new_col

            new_state = list(state)

            
            new_state[zero_index], new_state[new_index] = \
                new_state[new_index], new_state[zero_index]

            neighbors.append(tuple(new_state))

    return neighbors
def solve(start):

    priority_queue = []
    heappush(priority_queue, (heuristic(start), 0, start, [start]))

    visited = set()

    while priority_queue:

        f, g, state, path = heappop(priority_queue)

        if state in visited:
            continue

        visited.add(state)
        if state == GOAL:
            return path

        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None
def print_puzzle(state):

    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])

    print()
print("Enter the initial state")
print("Use 0 for the blank space")

values = []

for i in range(9):
    value = int(input("Enter value " + str(i + 1) + ": "))
    values.append(value)

start = tuple(values)

print("\nInitial State:")
print_puzzle(start)

solution = solve(start)

if solution is None:

    print("No solution found.")

else:

    print("Solution found!")
    print("Number of moves:", len(solution) - 1)
    print()

    for step, state in enumerate(solution):

        print("Step", step)
        print_puzzle(state)
