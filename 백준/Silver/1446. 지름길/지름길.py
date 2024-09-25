import sys
from collections import defaultdict
INPUT = sys.stdin.readline

N, D = map(int, INPUT().split())
graph = defaultdict(list)
for _ in range(N):
  a, b, w = map(int, INPUT().split())
  graph[a].append((b, w))

dists = [i for i in range(D + 1)]
for i in range(D + 1):
  if i > 0:
    dists[i] = min(dists[i], dists[i - 1] + 1)
  
  if i in list(graph):
    for v, w in graph[i]:
      if v <= D and dists[v] > dists[i] + w:
        dists[v] = dists[i] + w

print(dists[D])