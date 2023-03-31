# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq
# 수영장
import sys
sys.stdin = open("input_03.txt", "r")

def dfs(n, sm):
    global ans
    if ans <= sm:   # 가지치기
        return

    if n>12:
        ans = min(ans, sm)
        return
    
    dfs(n+1, sm+day*lst[n])  # 일간권
    dfs(n+1, sm+mon)         # 월간권
    dfs(n+3, sm+mon3)        # 3개월권
    dfs(n+12, sm+year)       # 연간권

T = int(input())
for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0]+list(map(int, input().split()))

    # [1] 백트래킹
    # ans = 365*3000
    # dfs(1, 0)
    
    # [2] 규칙성 찾기
    s = [0] * 13
    for i in range(1, 13):
        # 가능한 방법 중 i달 까지의 최소비용
        s[i] = s[i-1]+day*lst[i]      # 일간권
        s[i] = min(s[i], s[i-1]+mon)  # 월간권
        if i >= 3:
            s[i] = min(s[i], s[i-3]+mon3) # 3개월권
        if i >= 12:
            s[i] = min(s[i], s[i-12]+year)# 연간권
    ans = s[12]

    print(f'#{tc} {ans}')