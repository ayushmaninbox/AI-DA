from collections import deque

def bfs_tree(tree, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        visited.append(node)
        queue.extend(tree.get(node, []))
    return visited

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
result = bfs_tree(tree, start_node)

print("BFS Traversal:", " → ".join(result))
