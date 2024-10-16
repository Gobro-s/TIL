import heapq as hq
from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
h = []
abs_dict = defaultdict(int)
hq.heapify(h)

for _ in range(n):
    m = int(input())
    
    if m != 0:
        hq.heappush(h,abs(m))
        abs_dict[m] += 1
            
    else:
        if h:
            tmp = hq.heappop(h)
            if abs_dict[-tmp] > 0:
                print(-tmp)
                abs_dict[-tmp] -= 1
            else:
                print(tmp)

        else:
            print(0)