# https://www.acmicpc.net/problem/10810

N, M = map(int, input().split())
bas = [0]*(N+1)

for _ in range(M):
    i, j, k  = map(int, input().split())
    for a in range(i, j+1):
        bas[a] = k

for i in range(1, N+1):
    print(bas[i], end = ' ')