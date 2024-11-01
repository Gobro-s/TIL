import sys

n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
stack = []
res = [0] * n

for i in range(n):
    if stack:
        while True:
            if top[i] <= stack[-1][0]:
                res[i] = stack[-1][1] + 1
                stack.append([top[i], i])
                break

            else:
                stack.pop()

            if not stack:
                stack.append([top[i], i])
                break

    else:
        stack.append([top[i], i])

print(*res)