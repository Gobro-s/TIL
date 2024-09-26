import sys
 
arr = []
cnt = 0  
#빈칸의 개수
found = False 

for _ in range(9):
    arr.append(list(sys.stdin.readline().split()))
 
blanks = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == '0':
            blanks.append((i, j))
            cnt += 1
 
 
def check(x, y, i):
    for p in range(9):
        # 행
        if arr[x][p] == i and p != y:
            return False
        # 열
        if arr[p][y] == i and p != x:
            return False
    # 3x3 체크
    square_x = 3 * (x // 3)
    square_y = 3 * (y // 3)
    for a in range(square_x, square_x + 3):
        for b in range(square_y, square_y + 3):
            if arr[a][b] == i:
                if a != x and b != y:
                    return False
    return True
 
 
def dfs(N):
    global found
    if N == cnt:  # 모든 빈칸을 채웠다면
        for i in range(9):
            print(*arr[i])
        found = True
        return
    else:
        # 빈칸에 하나씩 숫자 넣기
        x, y = blanks[N][0], blanks[N][1]
        for i in range(1, 10):
            arr[x][y] = str(i)
            if check(x, y, str(i)):
                dfs(N + 1)
            if found:
                return
        arr[x][y] = 0
        return
 
 
dfs(0)