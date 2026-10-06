from collections import deque

def water_jug():
    start = (0, 0)
    goal = (2, 0)

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        a, b = queue.popleft()

        if (a, b) == goal:
            break

        states = [
            (4, b),  
            (a, 3),  
            (0, b),  
            (a, 0),  
            (a - min(a, 3 - b),
             b + min(a, 3 - b)),

            # Pour 3L -> 4L
            (a + min(b, 4 - a),
             b - min(b, 4 - a))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                parent[state] = (a, b)
                queue.append(state)
    path = []
    state = goal

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()

    for state in path:
        print(state[0], state[1])

    print("Goal reached!")


water_jug()
