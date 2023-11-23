import heapq


def Dijkstra(graph, source):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weights in graph[current_vertex].items():
            distance = current_distance + weights

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


exemple_graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}

source_vertex = "A"

result_distances = Dijkstra(exemple_graph, source_vertex)

print(f"The Shortest distances from the source {source_vertex}.")
for vertex, distance in result_distances.items():
    print(f"{vertex}: {distance} .")
