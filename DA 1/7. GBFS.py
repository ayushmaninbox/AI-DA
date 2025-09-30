import heapq

def gbfs(graph, heuristics, start, goal):
    queue = []
    heapq.heappush(queue, (heuristics[start], [start]))
    visited = set()

    while queue:
        _, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (heuristics[neighbor], path + [neighbor]))
    return None

graph = {}
heuristics = {}

nodes = int(input("Enter number of nodes: "))
for _ in range(nodes):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (comma-separated): ").replace(" ", "")
    graph[node] = neighbors.split(",") if neighbors else []

for n in graph.keys():
    heuristics[n] = int(input(f"Heuristic for {n}: "))

start_node = input("Enter starting node: ")
goal_node = input("Enter goal node: ")

path = gbfs(graph, heuristics, start_node, goal_node)
if path:
    print("Path found:", " → ".join(path))
else:
    print("No path found.")
