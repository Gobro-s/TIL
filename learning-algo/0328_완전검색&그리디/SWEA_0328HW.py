import sys
sys.stdin = open("input.txt", "r")

from collections import Counter

T = int(input())
for tc in range(1, T+1):
    num, cnt = input().split()
    num, cnt = list(num), int(cnt)
    # if len(num) == 2:                        # 있어도 없어도 되네요
    #     if cnt % 2:
    #         num = reversed(num)
    #     print(f"#{tc} {''.join(num)}")
    #     continue
    # if not cnt:
    #     print(f"#{tc} {''.join(num)}")
    #     continue
    sort_num = sorted(num, reverse=True)  # 역순 정렬이 횟수 제한 없다면 가질 수 있는 최댓값
    dic = Counter(num)
    # print(dic)
    even = 0                    # 숫자 중복 여부(중복:1, 중복X:0)
    for i in dic.values():     # 중복이 있으면 얼만큼을 바꿔도 최댓값이 유지됨
        if i > 1:               # why? 자기들끼리 바꾸면 되니까.
            even = 1
    if num == sort_num:
        if even or not cnt % 2:
            print(f"#{tc} {''.join(num)}")
        elif cnt % 2:                          # 하지만 중복도 없고, 횟수도 홀수라면
            num[-1], num[-2] = num[-2], num[-1]   # 최댓값이 나와도 무조건 한번은 바꿔야 함
            print(f"#{tc} {''.join(num)}")       # 그래서 최소한으로 바꾸기 위해 가장 낮은 자릿수 변경
        continue
    ans = []
    check = dict()
    # print(check)
    def func(lst, count):
        global cnt
        if tuple(lst) in check:  # 중복 key값 가지를 싹둑싹둑
            return 0
        if count == cnt:
            return int(''.join(lst))
        # if ''.join(lst) == sort_num:        # 애초에 type이 달라 비교가 불가  
        #     return 0
        # print(tuple(lst))
        check[tuple(lst)] = 1
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                lst[i], lst[j] = lst[j], lst[i]
                ans.append(func(lst, count+1))    # 바꾼 횟수를 증가해줘야 하므로 count+1
                lst[i], lst[j] = lst[j], lst[i]
        return 0
    func(num, 0)
    # print(check)
    # print(ans)
    print(f'#{tc}', max(ans))