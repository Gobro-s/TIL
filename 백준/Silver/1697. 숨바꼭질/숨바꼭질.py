from collections import deque

Max = 100001
cnt = [0]*Max
n,k = map(int,input().split())
def bfs():
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if now == k:
            print(cnt[now])
            return
        for _next in (now+1,now-1,now*2):
            if 0<= _next <Max and not cnt[_next]:
                cnt[_next] = cnt[now]+1
                q.append(_next)
bfs()