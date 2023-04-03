N = int(input())
n_num = set(map(int, input().split()))
# 탐색 목표기 때문에 중복이든 아니든 노상관

M = int(input())
m_num = list(map(int, input().split()))

for i in range(M):
    if m_num[i] in n_num:
        print('1')
    else:
        print('0')