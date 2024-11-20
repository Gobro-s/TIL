import sys
total = int(sys.stdin.readline())
c = int(sys.stdin.readline())
answer = 0
for _ in range(c):
    cost, val = map(int, sys.stdin.readline().split())
    answer += cost * val
if answer == total:
    print('Yes')
else:
    print('No')