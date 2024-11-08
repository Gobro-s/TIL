import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split(" "))
check_list = list(map(int,sys.stdin.readline().split(" ")))
check_list.sort()
m_list = deque()
p_list = []

for i in check_list:
    if i < 0:
        m_list.append(i)
    else:
        p_list.append(i)

ans = 0
if not p_list:
    p_list.append(0)
if not m_list:
    m_list.append(0)

if abs(min(m_list)) < max(p_list):
    ans += p_list[-1]
    for i in range(m):
        if p_list:
            p_list.pop(-1)
        else:
            break
elif abs(min(m_list)) > max(p_list):
    ans += abs(m_list[0])
    for i in range(0,m):
        if m_list:
            m_list.popleft()
        else:
            break
else:
    if len(m_list) > len(p_list):
        ans += abs(m_list[0])
        for i in range(0, m):
            if m_list:
                m_list.popleft()
            else:
                break
    else:
        ans += p_list[-1]
        for i in range(m):
            if p_list:
                p_list.pop(-1)
            else:
                break

for i in range(0,len(m_list),m):
    ans += (abs(m_list[i]) * 2)
for i in range(len(p_list)-1,-1,-m):
    ans += (p_list[i] * 2)
print(ans)