import heapq
import math


def traveling_salesman(graph):
    num_cities = len(graph)
    # Create a priority queue to store the minimum bound and the current path
    pq = []
    # Initialize the priority queue with the starting city as the current path and a bound of 0
    heapq.heappush(pq, (0, [0], set([0])))
    # Initialize the minimum distance to infinity
    min_distance = float('inf')

    while pq:
        # Get the minimum bound and current path from the priority queue
        bound, path, visited = heapq.heappop(pq)
        # If the bound is greater than or equal to the minimum distance, continue to the next iteration
        if bound >= min_distance:
            continue
        # If we've visited all cities, calculate the distance and update the minimum distance if necessary
        if len(path) == num_cities:
            distance = calculate_distance(path, graph)
            min_distance = min(min_distance, distance)
            continue
        # Explore all possible paths from the current city
        for next_city in range(num_cities):
            if next_city not in visited:
                # Calculate the new bound by adding the minimum distances to the remaining unvisited cities
                new_bound = bound + \
                    calculate_min_distance(path[-1], next_city, graph, visited)
                # Add the new path to the priority queue
                new_path = path + [next_city]
                new_visited = visited | set([next_city])
                heapq.heappush(pq, (new_bound, new_path, new_visited))

    return min_distance


def calculate_distance(path, graph):
    # Calculate the total distance of the path by summing the distances between each pair of consecutive cities
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i+1]]
    distance += graph[path[-1]][path[0]]
    return distance


def calculate_min_distance(city, next_city, graph, visited):
    # Calculate the minimum distance from the current city to the next unvisited city
    min_distance = float('inf')
    for i in range(len(graph)):
        if i != city and i not in visited:
            min_distance = min(min_distance, graph[city][i])
    return min_distance


# Example usage
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
min_distance = traveling_salesman(graph)
print("Minimum Distance :", min_distance)
