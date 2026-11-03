colors = ["Red", "Green", "Blue"]

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

assigned = {}

def is_safe(region, color):
    for neighbor in graph[region]:
        if neighbor in assigned and assigned[neighbor] == color:
            return False
    return True

def solve(region):
    if region == len(graph):
        return True

    area = list(graph.keys())[region]

    for color in colors:
        if is_safe(area, color):
            assigned[area] = color

            if solve(region + 1):
                return True

            del assigned[area]

    return False

print("Map Coloring using CSP")
print("\nMap Regions and Neighbors:")

for area, neighbors in graph.items():
    print(area, ":", neighbors)

if solve(0):
    print("\nMap Coloring Solution:")
    for area, color in assigned.items():
        print(area, ":", color)
else:
    print("No solution exists")
