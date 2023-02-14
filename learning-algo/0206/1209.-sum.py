import sys
sys.stdin = open("input (1).txt", "r")


T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_a = 0
    sum_list = []
    #가로행
    for i in range(100):
        for j in range(100):
            sum_a += arr[i][j]
        sum_list.append(sum_a)
        sum_a = 0

    #열
    for i in range(100):
        for j in range(100):
            sum_a += arr[j][i]
        sum_list.append(sum_a)
        sum_a = 0

    #대각선(우->좌)
    for k in range(100):
        for k in range(100):
            sum_a += arr[k][99-k]
        sum_list.append(sum_a)
        sum_a = 0

    #대각선(우<-좌)
    for i in range(100):
        sum_a += arr[i][i]
    sum_list.append(sum_a)


    print(f'#{test_case} {max(sum_list)}')