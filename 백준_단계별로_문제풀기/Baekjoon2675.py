# https://www.acmicpc.net/problem/2675

T = int(input())
for tc in range(1, T+1):
    R, word = input().split()
    R = int(R)
    for i in word:
        print(i*R, end = "")
    print()
