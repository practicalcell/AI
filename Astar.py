import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {start: 0}

    while open_list:
        f_cost, current = heapq.heappop(open_list)

        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            return path[::-1]

        for neighbour, cost in graph[current]:
            new_g_cost = g_cost[current] + cost

            if neighbour not in g_cost or new_g_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_g_cost

                # f(n) = g(n) + h(n)
                f_cost = new_g_cost + heuristic[neighbour]

                heapq.heappush(open_list, (f_cost, neighbour))
                came_from[neighbour] = current

    return None


# Graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2), ('E', 4)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}

# Find path
path = a_star(graph, 'A', 'G', heuristic)

print("Shortest path:", path)