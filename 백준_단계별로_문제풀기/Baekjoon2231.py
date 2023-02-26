# https://www.acmicpc.net/problem/2231

N = int(input())

ans = 0
for i in range(1, N+1):
    ans = list(map(int, str(i)))

    rlt = sum(ans)+i
    if rlt == N:
        print(i)
        break
    elif i == N:
        print('0')