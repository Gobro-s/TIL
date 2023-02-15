# https://www.acmicpc.net/problem/8958

T = int(input()) # 테스트 케이스 개수

for test_case in range(1, T+1): # T개 만큼의
    OX = list(input()) # ox 표 인풋
    score = 0  # score초기값
    sum_ = 0  # 합계 초기값
    for i in OX:
        if i == 'O':
            score += 1 # 연속해서 있으면 +1점씩 커지는 점수
            sum_ += score # 점수 합계에 점수 누적
        else: # O 아니면( i == 'X')
            score = 0 # 점수는 0으로 초기화
    print(sum_) # (tc 안에서 출력해야 함)