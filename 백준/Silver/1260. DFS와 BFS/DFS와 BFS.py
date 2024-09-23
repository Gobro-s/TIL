import sys
from collections import deque

sys.setrecursionlimit(10000)

n, m, start = map(int, sys.stdin.readline().split())
graph = {}

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    if u in graph:
        graph[u].append(v)
        graph[u].sort()
    else:
        graph[u] = [v]
    if v in graph:
        graph[v].append(u)
        graph[v].sort()
    else:
        graph[v] = [u]

def dfs(u):
    visited[u] = True
    res.append(u)
    if u in graph:
        for v in graph[u]:
            if not visited[v]:
                dfs(v)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        u = queue.popleft()
        res.append(u)
        if u in graph:
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)

visited = [False for _ in range(n+1)]
res = []
dfs(start)
print(*(res))

visited = [False for _ in range(n+1)]
res = []
bfs(start)
print(*(res))