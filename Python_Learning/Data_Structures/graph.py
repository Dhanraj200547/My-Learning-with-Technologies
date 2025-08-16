#using adjacency list
edges = [
    (0, 1),
    (0, 5),
    (1, 2),
    (1, 4),
    (2, 3),
    (3, 4),
    (4, 5)
]
n = len(edges) - 1
graph = [[] for _ in range(n)]
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
print(graph)