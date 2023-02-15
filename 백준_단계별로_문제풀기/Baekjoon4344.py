# https://www.acmicpc.net/problem/4344

C = int(input())

for test_case in range(1, C+1):
    N = list(map(int, input().split()))
    avr = sum(N[1:]) / N[0]  # N[1 ~]은 점수 N[0]은 학생 수

    cnt = 0
    for i in N[1:]:
        if i > avr:
            cnt += 1
        else:
            pass
    pct = round(cnt/N[0] *100, 3)

    print(f'{pct:.3f}%')