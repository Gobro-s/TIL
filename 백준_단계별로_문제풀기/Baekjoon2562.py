# https://www.acmicpc.net/problem/2562

numbers = []

for _ in range(9):
    i = int(input())
    numbers.append(i)

max_ = max(numbers)
print(max_)
mx = numbers.index(max_)
print(mx + 1)