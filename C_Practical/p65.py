def primes(graph:list,sour:int):
    V=len(graph)
    res=V*[V*[0]]
    vert=[{"w":w,"n":[sour,i]}  for i,w in enumerate(graph[sour]) if w>0 ]
    visited=[sour]
    while len(vert)>0 and len(visited)<V:
        vert.sort(key="w")
        mi=vert[0]
        if mi[]:
        res[mi["n"][0]][mi["n"][1]]=min["w"]
        vert+=[{"w":w,"n":[sour,i]}  for i,w in enumerate(graph[sour]) if w>0 ]


    return res

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

primes(graph,0)