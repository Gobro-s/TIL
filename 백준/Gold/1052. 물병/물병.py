import sys

input = sys.stdin.readline

N, K = map(int, input().split())

n = N
cnt = 0

while bin(n).count('1') > K:
    tmp = bin(n)
    idx = len(tmp) - tmp.rfind('1') - 1
    cnt += (1 << idx)

    n = n + (1 << idx)

print(cnt)