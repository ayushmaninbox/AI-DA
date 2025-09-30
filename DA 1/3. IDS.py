def dls(tree, node, goal, limit, visited):
    if node == goal:
        return [node]
    if limit <= 0:
        return None
    visited.append(node)
    for child in tree.get(node, []):
        if child not in visited:
            path = dls(tree, child, goal, limit - 1, visited.copy())
            if path:
                return [node] + path
    return None

def ids(tree, start, goal, max_depth):
    for depth in range(max_depth + 1):
        path = dls(tree, start, goal, depth, [])
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
max_depth = int(input("Enter max depth limit: "))

result = ids(tree, start_node, goal_node, max_depth)

if result:
    print("Path found:", " → ".join(result))
else:
    print("No path found within depth limit")
