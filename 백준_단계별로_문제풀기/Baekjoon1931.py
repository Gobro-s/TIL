# https://www.acmicpc.net/problem/1931

import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
cnt = 0

last = -1

for i in arr:
    if i[0] >= last:
        cnt += 1
        last = i[1]

print(cnt)
