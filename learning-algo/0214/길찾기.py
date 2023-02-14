import sys
sys.stdin = open("길찾기_input.txt", "r")

for _ in range(10):
    test_case, E = map(int, input().split())
    data = list(map(int, input().split()))
    arr = [0] * 101
    visited = []

    for i in range(E):
        n1, n2 = data[i * 2], data[i * 2 + 1]
        arr[n1][n2] == 1
        arr[n2][n1] == 1

    stack = []






