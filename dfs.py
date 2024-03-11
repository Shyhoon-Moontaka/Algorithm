def DFS(graph, root):
    visited = []
    stack = [root]
    while stack:
        node = stack.pop()
        visited.append(node)
        for child in reversed(graph[node]):
            if child not in visited and child not in stack:
                stack.append(child)
    return visited

graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 4], 3: [0], 4: [2]}
print(DFS(graph, 0))
