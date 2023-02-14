# https://www.acmicpc.net/problem/10818

N = int(input())

nums = list(map(int, input().split()))

max_ = max(nums)
min_ = min(nums)


print(min_, max_, end = ' ')

