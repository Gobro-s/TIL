import heapq as h
import sys
input=sys.stdin.readline

n=int(input())
a=sorted([list(map(int, input().split()))[1:] for _ in range(n)])
r=[a[0][1]] 

for S,E in a[1:]:
    if S>=r[0]:h.heappop(r)
    h.heappush(r,E)

print(len(r))