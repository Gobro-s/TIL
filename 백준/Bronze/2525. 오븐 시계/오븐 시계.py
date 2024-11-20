import sys
H, M = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline())

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
