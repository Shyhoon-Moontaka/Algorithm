class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=[]
    def addEdge(self,s,d,w):
        self.graph.append([s,d,w])
    def printSolution(self,dist):
        for i in range(self.V-1):
            print(i," ",dist[i])
    def bellmanFord(self,src):
        dist=[float('inf')]*self.V
        dist[src]=0
        for _ in range(self.V-1):
            for s,d,w in self.graph:
                if dist[s]!=float('inf') and dist[s]+w<dist[d]:
                    dist[d]=dist[s]+w
        for s,d,w in self.graph:
            if dist[s]!=float('inf') and dist[s]+w<dist[d]:
                print("negative cycle detected")
                return
        self.printSolution(dist)
g = Graph(5)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 4)
g.addEdge(1, 3, 3)
g.addEdge(2, 1, 6)
g.addEdge(3, 2, 2)

g.bellmanFord(0)
