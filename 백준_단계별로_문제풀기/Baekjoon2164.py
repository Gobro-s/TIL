from collections import deque

N = int(input())
deq = deque([i for i in range(1, N+1)])

while len(deq) > 1:
    deq.popleft()
    num = deq.popleft()
    deq.append(num)
print(deq[0])