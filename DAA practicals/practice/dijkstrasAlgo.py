import heapq


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    paths = {node: [] for node in graph}
    paths[start] = [start]

    heap = [(0, start)]

    while heap:
        (distance, current_node) = heapq.heappop(heap)

        if current_node == end:
            return (distances[current_node], paths[current_node])

        if distance > distances[current_node]:
            continue

        for neighbour, weight in graph[current_node].items():
            print(neighbour, weight)

        for neighbour, weight in graph[current_node].items():
            tentative_distance = distance+weight
            if tentative_distance < distances[neighbour]:
                distances[neighbour] = tentative_distance
                paths[neighbour] = paths[current_node]+[neighbour]
                heapq.heappush(heap, (tentative_distance, neighbour))

    return (None, None)


graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {'E': 6},
    "E": {}
}

start_node = 'A'
end_node = 'E'

shortest_distance, shortest_path = dijkstra(graph, start_node, end_node)

if shortest_distance is not None:
    print(
        f"The shortest path from {start_node} to {end_node} is {shortest_path} with a distance of {shortest_distance}.")
else:
    print(f"There is no path from {start_node} to {end_node}.")
