# N = X^3 찾아라
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    x = int(input()) ** (1/3)
    ans = round(x)
    print(f'#{tc} {ans}')