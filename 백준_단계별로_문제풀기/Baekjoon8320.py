# https://www.acmicpc.net/problem/8320

# i * j <= N: cnt += 1  직사각형 1 을 넓이라고생각

N = int(input())

cnt = 0
for i in range(1, N+1):
    for j in range(1, i+1):
        if i * j <= N:
            cnt += 1
        else:
            break

print(cnt)