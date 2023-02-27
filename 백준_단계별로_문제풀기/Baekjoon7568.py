# https://www.acmicpc.net/problem/7568

N = int(input()) # 전체 사람들
lst = [] # 학생 리스트

for _ in range(N):
    wei, hei = map(int, input().split())
    lst.append((wei, hei))

for i in lst:
    rank = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")