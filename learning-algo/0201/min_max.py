# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
# import sys
#
# sys.stdin = open("input.txt")
'''
입력
첫 줄에 T(1 <= T <=50)
다음 줄에 N개의 양수 ai가 (1 <= ai <= 1000000)
'''

T = int(input())   # Test_case T를 입력 받는다.

for i in range(T):  # 입력받은 T 만큼 반복
    N = int(input())  # N을 정수로 입력 받는다.
    ais = list(map(int, input().split()))  # N만큼 양수 as를 입력 받는다.

    # max_ = 0
    # min_ = 1000001
    #
    # for j in ais:
    #     if j > max_:
    #         max_ = j
    #     if j < min_:
    #         min_ = j

    # ais의 최댓값 구하기
    max_ = ais[0]
    for j in range(1, N):
        if max_ < ais[j]:
            max_ = ais[j]



    # ais의 최솟값 구하기
    min_ = ais[0]
    for k in range(1, N):
        if min_ > ais[j]:
            min_ = ais[j]


    dif = ((max_)-(min_))



    print(f'#{i+1} {dif}')