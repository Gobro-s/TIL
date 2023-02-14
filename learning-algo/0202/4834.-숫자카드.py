T = int(input()) 

for tc in range(T):
    N = int(input())
    numbers = list(map(int, input()))

#최대 숫자 찾기
    maxnum = numbers[0]
    for i in numbers:
        if i > maxnum:
            maxnum = i
    # print(maxnum)      ----------> 최댓값 출력까진 확인
    
    
##최대 숫자의 장 수 찾기
    counts = [0] * (maxnum+1)
    for j in range(1, N):
        max_card = 0
        max_num = 0

    








    
# print(f'#{num} {cards}')