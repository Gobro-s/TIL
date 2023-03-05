# https://www.acmicpc.net/problem/1018

N, M = map(int, input().split())

arr = [list(map(str,input())) for _ in range(N)]

cnt = 0
for i in range(M):
    for j in range(N):
        if arr[0][0] == 'W':
