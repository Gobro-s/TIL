import sys
# 파일 불러와서 테스트 케이스 받아오기.
sys.stdin = open("input.txt")


T = int(input())

for i in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(numbers)
