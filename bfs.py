def BFS(graph, root):
    visited = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        visited.append(node)
        for child in graph[node]:
            if child not in visited and child not in queue:
                queue.append(child)
    return visited

graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 4], 3: [0], 4: [2]}
print(BFS(graph, 0))