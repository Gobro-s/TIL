# https://www.acmicpc.net/problem/1018

N, M = map(int, input().split())

arr = [input() for _ in range(N)]


res = []

for i in range(N-7):         # 8X8로 잘라낸다고 했으니까
    for j in range(M-7):
        draw_W = 0   # 하얀색으로 시작하는 판
        draw_B = 0   # 깜장색으로 시작하는 판
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y)%2:
                    if arr[x][y] != 'W':
                        draw_W += 1
                    else:
                        draw_B += 1
                else:
                    if arr[x][y] != 'B':
                        draw_W += 1
                    else:
                        draw_B += 1

        res.append(draw_B)
        res.append(draw_W)

print(min(res))