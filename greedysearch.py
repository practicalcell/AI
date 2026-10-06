import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))

    visited = set()

    while priority_queue:
        h, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        print(current, end=" ")
        visited.add(current)

        if current == goal:
            print("\nGoal found!")
            return

        for neighbour in graph[current]:
            if neighbour not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbour], neighbour)
                )

    print("\nGoal not found!")


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

# Start search
greedy_best_first_search(graph, 'A', 'G', heuristic)