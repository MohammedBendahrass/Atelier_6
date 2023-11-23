def bellman_ford(graph, source):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[source] = 0

    for i in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight

    return distances


exemple_graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}

source_vertex = "A"

result_distances = bellman_ford(exemple_graph, source_vertex)

print(f"The Shortest distances from the source {source_vertex}.")
for vertex, distance in result_distances.items():
    print(f"{vertex}: {distance} .")
