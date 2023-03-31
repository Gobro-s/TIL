# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB
# 격자판의 숫자 이어 붙이기
# 중복 제거: set()
# n : 자리번호(1~7) |1|(자리번호)001000
# 2번째 자리 숫자 (상 하 좌 우 선택) -> 항상 선택 가능? ->X -> 이동이 범위 내일 경우만 가능
# 결국 가능한 모든 경우..... n==7까지 중복제거 -> set() 추가
'''
dfe(n, tstr, ci, cj)
    if n==7:
        sset.add(tstr)
        return
for di, dj in (상하좌우)
    ni, nj <- 계산
    if 범위 내라면
    dfs(n+1, tstr+[arr[ni][nj]],ni,nj)
'''

import sys
sys.stdin = open("input_04.txt", "r")

def dfs(n, tst, ci, cj):
    if n == 7:
        sset.add(tst)  # 중복제거
        return

    for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
        ni, nj = ci+di, cj+dj
        if 0<= ni < 4 and 0 <= nj < 4:
            dfs(n+1, tst+ arr[ni][nj], ni, nj)

T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    sset = set()
    
    for i in range(4):
        for j in range(4):
            dfs(1, arr[i][j], i, j)

    ans = len(sset)
    print(f'#{tc} {ans}')