import sys
import heapq
N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    a = int(sys.stdin.readline())
    heapq.heappush(numbers,a)
count = 0

for i in range(N-2):
    a = heapq.heappop(numbers)
    b = heapq.heappop(numbers)
    count += (a + b)
    heapq.heappush(numbers,a+b)
if len(numbers) == 1:
    print(0)
else:
    count += (sum(numbers))
    print(count)
        
