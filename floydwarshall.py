INF=999
def floydwarshall(graph):
    v=len(graph)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    for i in range(v):
        for j in range(v):
            if graph[i][j]=="INF":
                print("INF",end=" ")
            else:
                print(graph[i][j],end=" ")
        print(" ")
G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
floydwarshall(G)

