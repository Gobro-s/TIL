# https://www.acmicpc.net/problem/1546

N = int(input())   #시험 본 갯수
score = list(map(int,input().split()))  # 원래 시험 점수
max_ = max(score) # 원래 점수 중 최고점

nscore = []  # 새로운 평균을 받을 리스트 생성
for i in score: # 반복문을 통해 원래 평균에 조작을 가함
    nscore.append(i / max_ * 100)
avr = sum(nscore) / N # 새로운 평균 구하기
print(avr)