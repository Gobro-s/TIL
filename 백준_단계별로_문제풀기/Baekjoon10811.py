# https://www.acmicpc.net/problem/10811

N, cnt = map(int, input().split())
arr = []
for i in range(N):
    arr.append(i+1)   # 바구니 완 성!

for _ in range(cnt):
    i, j = map(int, input().split())
    tmp = arr[i-1:j]
    tmp.reverse()
    arr[i-1:j] = tmp

print(*arr)
            