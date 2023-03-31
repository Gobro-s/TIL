# https://www.acmicpc.net/problem/15650

nums = []
def f(s):   # 시작 지점 정해주고
    if len(nums) == M:     # 주어진 M과 수열의 길이가 같다면
        print(*nums)       # print 하쇼
        return
    for i in range(s, N+1):   # s부터 N까지 도는동안
        if i not in nums:     # i가 nums에 없다면
            nums.append(i)    # 추가 해보고
            f(i+1)               # 함수 재 호출 하고 (+1해서)
            nums.pop()        # 계속 쌓이지 않게 빼줘


N, M = map(int, input().split())

f(1)