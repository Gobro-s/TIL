import sys
sys.stdin = open("carrot_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    # carrot = [0] * (N-1)

    cnt = 1
    ans = 1
    for i in range(N-1):

        if i+1 <= N:

            if C[i] < C[i+1]:

                cnt += 1
                ans = cnt

                # print(cnt)
            if C[i] >= C[i+1]:

                cnt = 1
                # carrot.append(carrot)

    # print(cnt)
# cnt =
# cnt.sort()
# max_cnt = cnt[-1]
#
#
#     #
#     #
#     #
#     #
    print(f'#{test_case} {ans}')