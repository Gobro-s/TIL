import sys
sys.stdin = open("nqueen_input.txt", "r")

def promising(i, j):
    for di, dj in [[-1,-1], [-1, 0], [-1, 1]]:
        ni, nj = i+di, j+dj
        while 0 <= ni <N and 0 <= nj < N:
            if arr[ni][nj]:      # 다른 퀸이 이미 있는 상황
                return 0         # 실패 ! 
            ni, nj = ni+di, nj+dj  # 그렇지 않으면 다시 다음 자리로 이동해봐
    return 1                     # arr[i][j] 에 퀸을 놓을 수 있음

def f(i, N):
    global cnt
    if i == N:    # N개의 퀸을 놓은 경우
        cnt += 1
    else:
        for j in range(N):
            if promising(i, j):
                arr[i][j] = 1
                f(i+1, N)
                arr[i][j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    cnt = 0
    f(0, N)
    print(f'#{tc} {cnt}')