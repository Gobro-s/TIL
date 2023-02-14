T = int(input())
#d = 두 기차 사이 거리
#a = 기차 A의 속력
#b = 기차 B의 속력
#f = 파리의 속력    
# 거 = 시x속
for test_case in range(1, T+1):
    d, a, b, f = map(int, input().split())

    time = d / (a + b)
    distance = time * f
    
    print(f'#{test_case} {distance}')