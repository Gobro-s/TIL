import sys
sys.stdin = open("GNS_test_input.txt", "r")

T = int(input())
# 비교 할 정렬된 리스트
num_alpha = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for test_case in range(1, T+1):
    N = list(map(str, input().split()))
    # print(N)
    unordered = list(map(str, input().split()))

    cnt = [0] * 10
    # print(cnt)
    for num in range(10):
        for j in unordered:
            if j == num_alpha[num]:
                cnt[num] += 1
    # print(cnt)
    print(f'#{test_case}')
    for i in range(10):
        #print(f'i {i}')
        for k in range(cnt[i]):
            #print(f'k {k}')
            print(num_alpha[i], end=' ')

    print()