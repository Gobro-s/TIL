import sys
n, x = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
answer = []
for i in lst:
    if i < x:
        answer.append(i)
for j in answer:
    print(j)