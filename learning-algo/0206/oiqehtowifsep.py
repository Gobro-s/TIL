import sys
sys.stdin = open("input (1).txt", "r")
N = 3
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)