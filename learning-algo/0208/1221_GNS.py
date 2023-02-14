import sys
sys.stdin = open("GNS_test_input.txt", "r")

T = int(input())
num_alpha = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for test_case in range(1, T+1):
    N = list(map(str, input().split()))
    unordered = list(map(str, input().split()))

    ordered = []
    for i in range(10):
        for j in num_alpha:
            if num_alpha[i] == j:
                ordered.append(j)
        print()



    print(f'#{test_case}' {})






