# https://www.acmicpc.net/problem/2738

N, M = map(int, input().split())

A = [[0] for _ in range(N)]
B = [[0] for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))

for j in range(N):
    B[j] = list(map(int, input().split()))

for r in range(N):
    for c in range(M):
        print(A[r][c] + B[r][c], end = ' ')


    print()