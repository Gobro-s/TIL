# https://www.acmicpc.net/problem/2738

N, M = map(int, input().split())

A = [0 for _ in range(N)]
B = [0 for _ in range(M)]
for i in range(N):
    A[i] = list(map(int, input().split()))

for j in range(M):
    B[j] = list(map(int, input().split()))

print(A)
print(B)
# for i in range(N):
#     for j in range(M):
#         print(A[i][j] + B[i][j], end = ' ')


#     print()
