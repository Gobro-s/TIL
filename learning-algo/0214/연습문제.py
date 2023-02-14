'''
7 8 (V, E)
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

'''

# V(정점), E(간선)
V, E = map(int, input().split())

data = list(map(int, input().split()))
# 반복문에서 꺼내오는 값을 안 쓸 때에는 보통 _ 사용
arr = [[0] * (V + 1) for _ in range(V + 1)]

visited = [0] * (V+1) # 방문 여부 확인하는 List


for i in range(E):
	n1, n2 = data[i*2], data[i*2+1]
	arr[n1][n2] = 1 # n1과 n2는 인접해있다.
	arr[n2][n1] = 1 # 방향이 지정 되어 있지 않으므로 양쪽 입력


def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    # 현재 v는 시작정점, 인접한 정점 중 방문을 안한 곳

    for w in range(1, V + 1):

        # 지금 현재 정점에서 다음 정점으로 연결되어 있고, 방문을 안했느냐?
        if arr[v][w] == 1 and visited[w] == 0:
            # 방문 했다고 도장 찍기 위해 재귀를 한번 더 호출하는 것임
            dfs(w)


dfs(1)