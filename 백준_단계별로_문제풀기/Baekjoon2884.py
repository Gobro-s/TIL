# https://www.acmicpc.net/problem/2884

H, M = map(int, input().split())

#45분보다 작을 때
if M < 45:
# 만약 00시라면
    if H == 0:
        # 한 시간 빼주고
        H = 23
        # 60분을 더한다. (후에 45분 제한다.)
        M += 60
    else:
        # 그게 아니라면 한시간 빼고
        H -= 1
        # 60분 더한다.( 후에 45분 제한다.)
        M += 60

print(H, M-45)
