import heapq
import os


def clrscr():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


clrscr()

# --------------------  Implemetation  --------------------


def dijkstra(graph, start, end):
    """
    Computes the shortest distances from the start node to all other nodes in the graph using Dijkstra's algorithm with min-heap priority queue.
    :param graph: A dictionary of dictionaries representing the graph, where graph[u][v] is the weight of edge (u,v).
    :param start: The source node
    :param end: The destination node
    :return: An array of nodes with the shortest path in sequence from source to destination
            An integer having the value of distance for that shortest path
    """
    # Set distance to all nodes as infinite
    distances = {node: float('inf') for node in graph}
    # Set distance to start node as 0
    distances[start] = 0

    # Initialize heap with starting node and its distance
    heap = [(0, start)]
    # Set initial values for previous nodes and visited nodes
    previous_nodes = {}
    visited = set()

    # Loop until heap is empty
    while heap:
        # Pop node with smallest distance from heap
        (current_distance, current_node) = heapq.heappop(heap)

        # If node has already been visited, skip it
        if current_node in visited:
            continue
        # Mark node as visited
        visited.add(current_node)

        # For each neighbour of the current node
        for neighbour, weight in graph[current_node].items():
            # Calculate the tentative distance from start node to neighbour node
            tentative_distance = current_distance + weight

            # If tentative distance is less than current distance to neighbour node, update distance
            if tentative_distance < distances[neighbour]:
                distances[neighbour] = tentative_distance

                # Set current node as the previous node for the neighbour node
                previous_nodes[neighbour] = current_node
                # Push neighbour node and its distance to the heap
                heapq.heappush(heap, (tentative_distance, neighbour))

    # If end node is not reachable, return None
    if end not in previous_nodes:
        return None, None

    # Build the shortest path by backtracking from end node to start node
    path = []
    current_node = end
    while current_node != start:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    path.insert(0, start)

    # Return the shortest distance and the path
    return distances[end], path


# --------------------  Usage  --------------------


# Consider the following graph in form of adjacency list as an example
graph = {
    'Home': {'Windmill': 2, 'Bank': 3},
    'Bank': {'Home': 3, 'Windmill': 2, 'Shopping mall': 1, 'Garage': 4},
    'Windmill': {'Home': 2, 'Bank': 2, 'Shopping mall': 3, 'Bar': 5},
    'Shopping mall': {'Bank': 1, 'Windmill': 3, 'School': 2},
    'Bar': {'Windmill': 5, 'School': 2},
    'Garage': {'Bank': 4, 'School': 1},
    'School': {'Garage': 1, 'Shopping mall': 2, 'Bar': 2}
}

start = 'Home'
end = 'School'

path, shortest_distance = dijkstra(graph, start, end)

print("Shortest path:", path)
print("Shortest distance:", shortest_distance)
