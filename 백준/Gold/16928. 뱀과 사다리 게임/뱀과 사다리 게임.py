from collections import deque

visited, maps = [0] * 101, [0] * 101
# 시작점 == 1
visited[1] = 1
N, M = map(int, input().split())
dice = [1, 2, 3, 4, 5, 6]
# 사다리
for _ in range(N):
    s, e = map(int, input().split())
    maps[s] = e
# 뱀
for _ in range(M):
    s, e = map(int, input().split())
    maps[s] = e

# BFS
queue = deque([1])
while queue:
    now = queue.popleft()
    # 주사위 굴리기(1~6)
    for d in dice:
        next = now + d
        if next > 100: continue
        if not visited[next]:
        	# 이동하게 될 칸에 사다리 또는 뱀이 있을 경우
            if maps[next]:
                next2 = maps[next]
                if not visited[next2]:
                    visited[next] = visited[now]+1
                    visited[next2] = visited[now]+1
                    queue.append(next2)
            else:
                visited[next] = visited[now]+1
                queue.append(next)
        if queue[-1] == 100:
            queue.clear()
            print(visited[now])