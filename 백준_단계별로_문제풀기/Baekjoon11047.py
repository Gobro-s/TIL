# https://www.acmicpc.net/problem/11047

# N = 동전 종류 가지 수
# K = 금액

N, K = map(int, input().split())   # N, K input받기

coin = []                          # list로 받아 index로 접근
for _ in range(N):                 
    coin.append(int(input()))
coin.sort(reverse=True)            # 역순으로 정렬해준다.

cnt = 0
while K > 0:                       # K == 0이면 다 거슬러 준것이므로,
    for i in range(N):             
        if coin[i] > K:            # coin의 금액이 K보다 크다면 못 거슬러줌
            continue
        else:                      # coin의 금액 < K라면 
            cnt += K//coin[i]      # K를 coin[i]로 나누고 몫을 취한다.
            K = K%coin[i]          # K는 나머지 값으로 재지정
        if K == 0:                 # K == 0 이라면 다 거슬러 준것이므로
            break                  # While문 탈출
            
print(cnt)