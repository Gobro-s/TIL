# https://www.acmicpc.net/problem/2750

N = int(input())
number = []
for i in range(1, N+1):
    num = int(input())
    number.append(num)

numbers = sorted(number)
for j in range(len(numbers)):
    print(numbers[j])