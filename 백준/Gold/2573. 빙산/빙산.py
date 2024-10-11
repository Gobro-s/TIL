from collections import deque
from copy import deepcopy
N,M=map(int,input().split())

room=[]
ice=[]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(N):
    data=list(map(int,input().split()))
    room.append(data)

    for j in range(M):
        if not data[j]==0:
            ice.append([i,j])



time=0
while True:
    tmp_room=deepcopy(room)
    tmp_ice=deepcopy(ice)
    #1. 빙산을  녹임.
    for x,y in ice:
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue

            if room[nx][ny]==0:
                if tmp_room[x][y]-1>0:
                    tmp_room[x][y]-=1
                elif tmp_room[x][y]-1==0:
                    tmp_room[x][y]=0
                    p=tmp_ice.index([x,y])
                    tmp_ice.pop(p)
    time+=1
    room=tmp_room
    ice=tmp_ice
   #만약 빙산이 다 녹았다면??
    zero=0
    for x in range(N):
        if room[x].count(0)==M:
            zero+=1

    if zero==N:
        time=0
        break
    #2. 녹인 빙산이 몇 덩어리인지 보기
    visited=[[False]*M for _ in range(N)]
    q=deque()
    dung=0
    out=0
    for x,y in ice:
        if visited[x][y]==True:
            continue
        dung+=1

        if dung>=2:
            out=1
            break
        q.append([x,y])
        visited[x][y]=True
        while q:
            px,py=q.popleft()

            for d in range(4):
                nx=px+dx[d]
                ny=py+dy[d]

                if nx<0 or nx>=N or ny<0 or ny>=M:
                    continue

                if visited[nx][ny]==True:
                    continue

                if room[nx][ny]==0:
                    continue

                q.append([nx,ny])
                visited[nx][ny]=True


    if out==1:
        break


print(time)