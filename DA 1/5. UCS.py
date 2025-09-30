import heapq

def ucs(graph, start, goal):
    queue = []
    heapq.heappush(queue, (0, start, [start]))
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))
    return None, None

graph = {}
nodes = int(input("Enter number of nodes: "))

for _ in range(nodes):
    node = input("Enter node: ")
    edges = input(f"Enter edges from {node} in format neighbor:weight (comma-separated, e.g., B:2,C:3): ").replace(" ", "")
    neighbors = []
    if edges:
        for edge in edges.split(","):
            n, w = edge.split(":")
            neighbors.append((n, int(w)))
    graph[node] = neighbors

start_node = input("Enter starting node: ")
goal_node = input("Enter goal node: ")

path, total_cost = ucs(graph, start_node, goal_node)

if path:
    print("Path found:", " → ".join(path))
    print("Total cost:", total_cost)
else:
    print("No path found.")
