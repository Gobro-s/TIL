N = int(input())
cnt = 0
six = 666
while True:
    if '666' in str(six):
        cnt+=1    # 몇 번째 666영화인지
    if cnt == N:  # 몇 번째랑 N이 동일 할 때
        print(six)   # six 뽑으슈
        break   # 반복문 탈출
    six +=1   