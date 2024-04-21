def dijkstra(graph, start):
    
    distances = {}
    for node in graph:
        distances[node] = float('infinity')
    distances[start] = 0
    
   
    visited = set()
    
    while len(visited) < len(graph):
       
        min_distance = float('infinity')
        min_node = None
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        
      
        visited.add(min_node)
        
        
        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances


graph = {
    'A': {'B': 3, 'C': 4, 'D': 7},
    'B': {'C': 1, 'F': 5},
    'C': {'F': 6, 'D': 2},
    'D': {'E': 3},
    'E': {'F': 1},
    'F': {}
}


start_node = 'A'


shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node)
for node, distance in shortest_distances.items():
    print("Node:", node, "Distance:", distance)
