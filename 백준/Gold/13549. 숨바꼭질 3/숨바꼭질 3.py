import sys
from collections import deque
from collections import defaultdict

# N = 수빈, K = 동생
N, K = map(int,sys.stdin.readline().split())

dirs = [-1, +1]
visit = defaultdict(bool)

dq = deque()
dq.append((N, 0))
visit[N] = True

# 애초에 같이 위치한다면
if N == K :
  print(0)
  exit()

while len(dq) != 0 :
  x, step = dq.popleft()

  if 0 <= x * 2 <= 100_000 and visit[x * 2] == False:
    if x * 2 == K:
      print(step)
      exit()
    visit[x * 2] = True
    dq.append((x * 2, step))

  for dir in dirs :
    next = x + dir
    if next == K :
      print(step + 1)
      exit()
    if 0<= next <= 100_000 and visit[next] == False:
      visit[next] = True
      dq.append( (next, step + 1 ) )