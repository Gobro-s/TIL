import sys
sys.stdin = open("input.xt", "r")

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def snail(x, y, N):
    # 시작점 == 1
    arr[x][y] =1
    # 델타검색 우측부터 시작
    idx = 0
