def dfs_tree(tree, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for child in tree.get(start, []):
        if child not in visited:
            dfs_tree(tree, child, visited)
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
result = dfs_tree(tree, start_node)

print("DFS Traversal:", " → ".join(result))
