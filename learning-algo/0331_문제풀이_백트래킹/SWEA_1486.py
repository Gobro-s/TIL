# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw
# 장훈이의 높은 선반

# ans<- N*10000
# dfs(n, sm  )
#   if n == N:
#       if sm >= B:
#           ans <- min(ans,sm-B)
#               return
# dfs(n+1, sm+lst[n])   # 포함
# dfs(n+1, sm)          # 미포함

def dfs(n, sm):    # sm = sum
    global ans
    ##### 최소값 구할 때 거의 항상 성공하는 가지치기 #####
    if ans <= sm-B:
        return
    if ans == 0:   # 이미 만점!
        return

    if n == N:
        if sm >= B:
            ans = min(ans,sm-B)
        return

    dfs(n+1, sm+lst[n])
    dfs(n+1, sm)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = N*10000
    dfs(0, 0)

    print(f'#{tc} {ans}')