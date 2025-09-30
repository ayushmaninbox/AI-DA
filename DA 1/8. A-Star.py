import heapq

def a_star(graph, heuristics, start, goal):
    queue = []
    heapq.heappush(queue, (heuristics[start], 0, [start]))
    g_cost = {start: 0}

    while queue:
        f, g, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path, g

        for neighbor, weight in graph.get(node, []):
            g_new = g + weight
            if neighbor not in g_cost or g_new < g_cost[neighbor]:
                g_cost[neighbor] = g_new
                f_new = g_new + heuristics[neighbor]
                heapq.heappush(queue, (f_new, g_new, path + [neighbor]))
    return None, None

graph = {}
heuristics = {}

nodes = int(input("Enter number of nodes: "))
for _ in range(nodes):
    node = input("Enter node: ")
    edges = input(f"Enter edges from {node} in format neighbor:weight (comma-separated): ").replace(" ", "")
    neighbors = []
    if edges:
        for edge in edges.split(","):
            n, w = edge.split(":")
            neighbors.append((n, int(w)))
    graph[node] = neighbors

for n in graph.keys():
    heuristics[n] = int(input(f"Heuristic for {n}: "))

start_node = input("Enter starting node: ")
goal_node = input("Enter goal node: ")

path, cost = a_star(graph, heuristics, start_node, goal_node)
if path:
    print("Path found:", " → ".join(path))
    print("Total cost:", cost)
else:
    print("No path found.")
