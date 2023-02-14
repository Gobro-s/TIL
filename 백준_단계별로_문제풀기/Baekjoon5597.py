# https://www.acmicpc.net/problem/5597

numbers = [number for number in range(1, 31)]

for _ in range(28):
    num = int(input())
    numbers.remove(num)

print(min(numbers), max(numbers), sep = '\n')