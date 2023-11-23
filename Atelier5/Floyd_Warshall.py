def floyd_warshall(graph):
    n = len(graph)
    distances = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    return distances


example_graph = [
    [0, 1, 4, float("inf")],
    [float("inf"), 0, 2, 5],
    [float("inf"), float("inf"), 0, 1],
    [float("inf"), float("inf"), float("inf"), 0],
]
result_distances = floyd_warshall(example_graph)

print(f"The shortest distances between all pairs of vertices .")

for row in result_distances:
    print(row)
