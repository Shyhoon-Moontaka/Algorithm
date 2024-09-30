def prims(graph,v):
    inf=999
    selected=[False]*v
    noEdge=0
    selected[0]=True
    while noEdge<v-1:
        minimum=inf
        x=y=0
        for i in range(v):
            if selected[i]:
                for j in range(v):
                    if not selected[j] and graph[i][j]:
                        if graph[i][j]<minimum:
                            minimum=graph[i][j]
                            x=i
                            y=j
        print(x," ",y," ",graph[x][y])
        selected[y]=True
        noEdge+=1
graph=[[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
v=5
prims(graph,v)
