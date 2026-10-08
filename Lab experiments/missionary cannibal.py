from collections import deque

def is_safe(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    # Left side
    if m > 0 and m < c:
        return False

    # Right side
    rm = 3 - m
    rc = 3 - c

    if rm > 0 and rm < rc:
        return False

    return True


def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    moves = [
        (1, 0),   # 1 missionary
        (2, 0),   # 2 missionaries
        (0, 1),   # 1 cannibal
        (0, 2),   # 2 cannibals
        (1, 1)    # 1 missionary + 1 cannibal
    ]

    while queue:
        state = queue.popleft()
        m, c, boat = state

        if state == goal:
            break

        for dm, dc in moves:

            if boat == 1:
                new_m = m - dm
                new_c = c - dc
                new_boat = 0
            else:
                new_m = m + dm
                new_c = c + dc
                new_boat = 1

            new_state = (new_m, new_c, new_boat)

            if is_safe(new_m, new_c) and new_state not in visited:
                visited.add(new_state)
                parent[new_state] = state
                queue.append(new_state)

    # Print solution
    path = []
    state = goal

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()

    for state in path:
        print(state)

solve()
