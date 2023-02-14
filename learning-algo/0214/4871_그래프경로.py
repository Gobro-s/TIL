import sys
sys.stdin = open("graphroute_input.txt", "r")

# s:출발 지점, n:다음 이동할 지점
def dfs(s):
    visited[s] = 1
    for n in range(1, V + 1):
        if arr[s][n] == 1 and visited[n] == 0:
            dfs(n)


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        i, j = map(int, input().split())
        arr[i][j] = 1

    s, e = map(int, input().split())

    dfs(s)
    result = 0
    if visited[s] == 1 and visited[e] == 1:
        result = 1

    print(f'#{test_case} {result}')

