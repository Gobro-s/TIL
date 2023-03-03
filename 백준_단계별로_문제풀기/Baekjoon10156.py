'''
과자 K원, 과자 개수 N, 현재 잔고 M
동수가 모자란 돈 계산

첫 줄에 K, N, M 이 공백 두고
'''

K, N, M = map(int, input().split())

money = K*N-M
if money > 0:
    print(money)

else:
    print(0)
