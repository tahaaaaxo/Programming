import heapq


def dijkstra(graph, start, end):
    # Create a dictionary to store the shortest distances to each node from the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Create a dictionary to store the shortest paths to each node from the start node
    paths = {node: [] for node in graph}
    paths[start] = [start]

    # Create a priority queue to store the nodes to be explored, with their tentative distances as the priority
    heap = [(0, start)]

    # Loop until all nodes have been explored or the shortest path to the end node has been found
    while heap:
        # Pop the node with the smallest tentative distance from the priority queue
        (distance, current_node) = heapq.heappop(heap)

        # If the current node is the end node, return the shortest path to it
        if current_node == end:
            return (distances[current_node], paths[current_node])

        # If the tentative distance to the current node is greater than the shortest distance found so far, skip it
        if distance > distances[current_node]:
            continue

        # Loop over the neighbors of the current node and update their tentative distances and paths if necessary
        for neighbor, weight in graph[current_node].items():
            tentative_distance = distance + weight
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(heap, (tentative_distance, neighbor))

    # If no path was found to the end node, return None
    return (None, None)


# Example usage
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {'E': 6},
    'E': {}
}

start_node = 'A'
end_node = 'E'

shortest_distance, shortest_path = dijkstra(graph, start_node, end_node)

if shortest_distance is not None:
    print(
        f"The shortest path from {start_node} to {end_node} is {shortest_path} with a distance of {shortest_distance}.")
else:
    print(f"There is no path from {start_node} to {end_node}.")
