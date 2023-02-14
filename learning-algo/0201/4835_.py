'''
첫 줄에 테스트 케이스 개수T
테스트케이스 첫줄에 정수의 개수 N과 구간의 개수M
다음줄에 정수 N개의 정수 ai개

'''

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    list_a = list(map(int, input().split()))

    nlist = []
    for j in range(N-M+1):
        sum_ = 0
        for k in range(0, M):
            sum_ += list_a[j+k]
        nlist.append(sum_)

    max_ = nlist[0]
    for j in range(1, len(nlist)):
        if max_ < nlist[j]:
            max_ = nlist[j]

    min_ = nlist[0]
    for k in range(1, len(nlist)):
        if min_ > nlist[j]:
            min_ = nlist[j]

    print(f'{i+1} {max_ - min_}')




# a = [1,2,3,4,5,6,7,8]
# a[1:3]
# [2,3]
# summ = 0
# 2
# 3
# summ
# 5
# nlist.a
# [5]











    #
    # print(f'{i+1}, {}')
