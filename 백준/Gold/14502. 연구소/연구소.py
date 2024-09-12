from copy import deepcopy
from itertools import combinations
from collections import deque

n,m =map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

#init
virus = []
slots=[]
for i in range(n):
    for j in range(m):
        if(maps[i][j]==2):
            virus.append((i,j))
        if(maps[i][j]==0):
            slots.append((i,j))

candidate = list(combinations(slots,3))

def check_safe(temp):
    global m,n
    res=0
    for i in range(n):
        for j in range(m):
            if(temp[i][j]==0):
                res+=1
    return res

def dfs_virus(temp):
    global virus,n,m
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    visited = [[0] * m for _ in range(n)]
    for i in virus:
        stack=[i]
        visited[i[0]][i[1]]=1
        while(stack):
            cur_r,cur_c = stack.pop()
            for i in range(4):
                nr = cur_r + dr[i]
                nc = cur_c + dc[i]
                if(nr>=n or nr<0 or nc>=m or nc<0):
                    continue
                if(temp[nr][nc]==1):
                    continue
                if(visited[nr][nc]==0):
                    temp[nr][nc]=2
                    visited[nr][nc]=1
                    stack.append((nr,nc))
    return temp

ans = -1

for i in candidate:
    temp = deepcopy(maps)
    for j in i:
        temp[j[0]][j[1]]=1
    ans = max(ans,check_safe(dfs_virus(temp)))

print(ans)