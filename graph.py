class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []
            return True
        return False

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacencyList and vertex2 in self.adjacencyList:
            self.adjacencyList[vertex1].append(vertex2)
            self.adjacencyList[vertex2].append(vertex1)
            return True
        return False

    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacencyList and vertex2 in self.adjacencyList:
            self.adjacencyList[vertex1].remove(vertex2)
            self.adjacencyList[vertex2].remove(vertex1)

    def removeVertex(self, vertex):
        
        for neighbor in self.adjacencyList[vertex]:
            self.removeEdge(vertex, neighbor)
        del self.adjacencyList[vertex] 
        for key in self.adjacencyList:
                if vertex in self.adjacencyList[key]:
                    self.adjacencyList[key].remove(vertex)
        return True
        
        

myGraph = Graph()
myGraph.addVertex("a")
myGraph.addVertex("b")
myGraph.addVertex("c")
myGraph.addEdge("a", "b")
myGraph.addEdge("b", "c")
myGraph.addEdge("c", "a")
myGraph.removeVertex("c")
print(myGraph.adjacencyList)
