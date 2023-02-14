T = int(input()) #횟수 input

for tc in range(T):
    num = int(input())# Babygin 확인할 숫자 input
    counts = [0] * 12 # 6자리 수로 부터 각 자리 수를 추출해 개수를 누적할 리스트

    for j in range(6):     #붙어 들어온 숫자를 한 자리씩 띄어 받기
        counts[num%10] += 1
        num//= 10

    i = 0
    tri = run = 0
    while i < 10:
        if counts[i] >= 3:  # triplete 조사 후 데이터 삭제
            counts[i] -= 3
            tri += 1
            continue
        if counts[i] >= 1 and counts[i+1] and counts[i+2] >= 1: #run 조사 후 데이터 삭제
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            run += 1
            continue
        i += 1
    
    if run + tri == 2:
        print('1')
    else:
        print('0')