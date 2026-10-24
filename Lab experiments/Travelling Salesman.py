
from itertools import permutations

n = int(input("Enter number of cities: "))

dist = []
for i in range(n):
    row = list(map(int, input("Enter distances: ").split()))
    dist.append(row)

cities = list(range(1, n))
min_cost = float('inf')
best_route = []

print("\nAll possible routes:")

for p in permutations(cities):
    route = [0] + list(p) + [0]
    cost = 0

    for i in range(len(route) - 1):
        cost += dist[route[i]][route[i + 1]]

    print("Route:", " -> ".join(chr(c + 65) for c in route),
          "| Cost:", cost)

    if cost < min_cost:
        min_cost = cost
        best_route = route

print("\nShortest route:",
      " -> ".join(chr(c + 65) for c in best_route))
print("Minimum cost:", min_cost)
