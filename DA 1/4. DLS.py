def dls(tree, node, goal, limit, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    if node == goal:
        return visited
    if limit <= 0:
        return None
    for child in tree.get(node, []):
        if child not in visited:
            path = dls(tree, child, goal, limit - 1, visited.copy())
            if path:
                return path
    return None

tree = {}
nodes = int(input("Enter number of nodes: "))

for _ in range(nodes):
    node = input("Enter node: ")
    children = input(f"Enter children of {node} (comma-separated, leave empty if none): ").replace(" ", "")
    if children:
        tree[node] = children.split(",")
    else:
        tree[node] = []

start_node = input("Enter starting node: ")
goal_node = input("Enter goal node: ")
depth_limit = int(input("Enter depth limit: "))

result = dls(tree, start_node, goal_node, depth_limit)

if result:
    print("Path found:", " → ".join(result))
else:
    print("No path found within depth limit")
