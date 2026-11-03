def minimax(depth, node, is_max):
    if depth == 2:
        return values[node]

    if is_max:
        best = -999
        for i in range(2):
            best = max(best, minimax(depth + 1, node * 2 + i, False))
        return best

    else:
        best = 999
        for i in range(2):
            best = min(best, minimax(depth + 1, node * 2 + i, True))
        return best

values = [3, 5, 2, 9]

result = minimax(0, 0, True)

print("Optimal value:", result)
