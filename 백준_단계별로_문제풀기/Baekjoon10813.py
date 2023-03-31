# https://www.acmicpc.net/problem/10813

N, cnt = map(int, input().split())   # N=바구니 cnt=공 바꾸는 횟수

arr = []
for i in range(N):
    arr.append(i+1)   # 바구니 완성

for _ in range(cnt):
    a, b = map(int, input().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]

print(*arr)
