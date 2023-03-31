# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7IzvG6EksDFAXB
# 부분 수열의 합
# 백트래킹 : 가능한 모든 경우를 다 해봐서 답을 냄.(단, 시간 초과 가능하므로 복잡도 미리 검토)
# 상태분간 트리. 트리 형태로 가능한 모든 경우를 펼쳐서 분석해본다.
# 재귀함수는 손으로 설계.
'''
1. 종료 조건 (n)
    n : 숫자번호(index)
2. tree(시각적) -> 2^20개.
3. ## n부터 N까지 모든 경우를 트리로 그려보고, n==N에 가서만 정답 조건 처리 하기
'''


import sys
sys.stdin = open("input_01.txt", "r")

def dfs(n, sm):
    global ans
    # [3] 가지치기 : 더 이상 정답 갱신 가능성 없는 경우
    # 가장 마지막에, 가장 윗쪽에 진행한다.
    if K < sm:
        return


    # [1] 종료조건(n에 관련): 반드시 정답처리는 이곳에서
    if n == N:
        if sm==K:
            ans += 1
        return
    
    # [2] 하부 호출
    dfs(n+1, sm+lst[n]) # 포함
    dfs(n+1, sm)       # 미포함


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = 0
    dfs(0,0)

    print(f'#{tc} {ans}')

    # 가지치기 전 우선 시간초과 나는지 확인 해보고, 초과가 난다면 그때 가지치기 해보며 연습.