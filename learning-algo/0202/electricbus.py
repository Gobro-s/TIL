# N 정류장 개수
# M 충전기 설치 정류장
# K 한번 충전으로 최대한 이동할 수 있는 정류장
# 도착을 못하면 return 0

T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    list_ = list(map(int, input().split()))
    
    a = 0 # 출발 지점
    b = 0 # 지나온 정류장의 갯수
    while True:
        
        m_list =[]
        for i in list_:
            if i <= (a + K):
                m_list.append(i)

        if not m_list: ## len(m_list) == 0
            break
        a = m_list[-1] # m_list의 최댓값.
        b += 1
        if a+K >= N:
            break
        
    print(b)