# https://www.acmicpc.net/problem/25304

X = int(input())  # 총 금액
N = int(input())  # 물건의 종류의 수

total = 0
for i in range(N):
    price, count = map(int, input().split())
    total += price*count

if total == X:
    print("Yes")
else:
    print("No")

