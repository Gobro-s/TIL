import sys
input = sys.stdin.readline

def bfs():
    r,c = map(int,input().split())
    board = [list(input().rstrip()) for _ in range(r)]

    move = [(0,1),(1,0),(0,-1),(-1,0)]
    result = 0
    q = set([(0,0,board[0][0])])
    while q:
        x,y,ch_list = q.pop()
        result = max(result,len(ch_list))
        if result==26:
            return 26

        for a,b in move:
            dx=x+a; dy=y+b
            if r>dx>=0 and c>dy>=0 and board[dx][dy] not in ch_list:
                q.add((dx,dy,ch_list + board[dx][dy]))
    return result
print(bfs())