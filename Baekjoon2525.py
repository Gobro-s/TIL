# https://www.acmicpc.net/problem/2525

H, M = map(int, input().split())
time = int(input())

plusH = (M + time)//60
midnight = (H + plusH -24)

if (M+time) < 60:
    print(H, M+time)

elif (M+time) % 60 == 0:
    if (H+plusH>=24):
        print(midnight, 0)
    else:
        print(H+plusH, 0)

elif (M+time)>60:
    if (H+plusH>=24):
        print(midnight, M+time-plusH*60)
    else:
        print(H + plusH, M+time - plusH*60)