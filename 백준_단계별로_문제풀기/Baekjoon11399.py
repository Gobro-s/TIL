# https://www.acmicpc.net/problem/11399

# n = 사람 수

n = int(input())
time = list(map(int, input().split()))


time.sort()

total = 0
for i in range(1, n+1):
    total += sum(time[0:i])

print(total)