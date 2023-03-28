# https://www.acmicpc.net/problem/11399

# n = 사람 수

n = int(input())
time = list(map(int, input().split()))


time.sort()  # 대기 시간이 짧을 수록 빨리 뽑을 수 있음

total = 0
for i in range(1, n+1):
    total += sum(time[0:i])  # 걸린 시간을 총 더해준다

print(total)