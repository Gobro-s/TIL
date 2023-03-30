import numpy as np

# https://www.acmicpc.net/problem/2740



N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

print(A)
print(B)