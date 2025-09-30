from collections import deque

def bfs_step(graph, queue, visited, other_visited):
    if queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                if neighbor in other_visited:
                    return neighbor
    return None

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    start_visited = set([start])
    goal_visited = set([goal])
    start_queue = deque([start])
    goal_queue = deque([goal])

    while start_queue and goal_queue:
        meet_node = bfs_step(graph, start_queue, start_visited, goal_visited)
        if meet_node:
            return start_visited, goal_visited, meet_node

        meet_node = bfs_step(graph, goal_queue, goal_visited, start_visited)
        if meet_node:
            return start_visited, goal_visited, meet_node

    return None, None, None

graph = {}
nodes = int(input("Enter number of nodes: "))

for _ in range(nodes):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (comma-separated): ").replace(" ", "").split(",")
    graph[node] = neighbors

start_node = input("Enter starting node: ")
goal_node = input("Enter goal node: ")

start_visited, goal_visited, meet_node = bidirectional_search(graph, start_node, goal_node)

if meet_node:
    print(f"Search met at node: {meet_node}")
    print("Start side visited:", " → ".join(start_visited))
    print("Goal side visited:", " → ".join(goal_visited))
else:
    print("No path found.")
