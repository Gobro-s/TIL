import sys
sys.stdin = open("newbus_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    bus_station = [0] * 1001


    # 버스 정보
    # [1, 2, 5]
    # [2, 3, 10]
    # [3, 2, 9]
    lst = [list(map(int, input().split())) for _ in range(N)]
    for bus in lst:
        A = bus[1] #출발
        B = bus[2] #종점

        # A와 B 정류장에는 반드시 정차한다.
        bus_station[A] += 1
        bus_station[B] += 1

        if bus[0] == 1:
            for i in range(A+1, B):
                bus_station[i] += 1

        # 출발지가 짝수
        elif bus[0] == 2:
        # 짝수, 홀수 관련 -> A + 2 (A 출발 정류소는 이미 방문했기 때문)
            for i in range(A + 2,B,2):
                bus_station[i] += 1

        # 홀/짝 관련 case 나누어서
        elif bus[0] == 3:
            if A % 2: # 홀수
                for i in range(A + 1, B):
                    if not (i % 3) and (i % 10):
                        bus_station += 1
            else: # 짝수
                for i in range(A + 1, B):
                    if not (i % 4): # 4의 배수로 나누면 나머지가 0임으로 부정연산자 not이 필요하다.

                        bus_station[i] += 1

    res = max(bus_station)
    print(f'#{test_case+1} {res}')



















    # print(f'#{test_case} {ans}')