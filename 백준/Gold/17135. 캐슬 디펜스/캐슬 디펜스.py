from itertools import combinations
import copy

x=[-1,0,1]
y=[0,-1,0]

def forward(map, m,n):
    for i in reversed(range(m-1)):
        map[i+1]=map[i]
    map[0]=[0 for _ in range(n)]
    return map
           
def get_comb(n):
    return combinations(range(n),3)

def get_distance(ori_y,ori_x,new_y,new_x):
    return abs(ori_y-new_y)+abs(ori_x-new_x)

def archure_bfs(map,m,n, archure_loc):
    killed_loc=set()
    kill_counter=0

    for archure in archure_loc:
        visit=[[0]*n for _ in range(m+1)]
        queue=[]
        queue.append((m,archure,0))
        now_distance=0

        visit[m][archure]=True
        find=False
        while queue and find==False:
            top=queue.pop(0)

            for i in range(3):
                newx=top[1]+x[i]
                newy=top[0]+y[i]
                if newx<0 or newx>=n or newy<0 or newy>=m or visit[newy][newx]==True:
                    continue
                now_distance=get_distance(m,archure,newy,newx)
                if now_distance<=distance:
                    if map[newy][newx]==1:
                        killed_loc.add((newy,newx))
                        visit[newy][newx]=True
                        find=True
                        break
                    else :
                        visit[newy][newx]=True
                        queue.append((newy,newx))

    for kill_loc in list(killed_loc):
        map[kill_loc[0]][kill_loc[1]]=0
        kill_counter+=1
        
    return kill_counter

m,n,distance=list(map(int,input().split()))
ori_map=[[0]*n for _ in range(m)]

for i in range(m):
    ori_map[i]=list(map(int,input().split()))

answer=0

comb=get_comb(n)

for idx, archure_loc in enumerate(comb):
    tmp_answer=0
    copy_map=copy.deepcopy(ori_map)
    
    for i in range(m):
        tmp_answer+=archure_bfs(copy_map,m,n,archure_loc)
        copy_map=forward(copy_map,m,n)
    answer=max(answer,tmp_answer)

print(answer)