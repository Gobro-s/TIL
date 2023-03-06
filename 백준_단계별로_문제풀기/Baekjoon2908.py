# https://www.acmicpc.net/problem/2908

num1, num2 = input().split()

num1 = int(num1[::-1])
num2 = int(num2[::-1])

lst = []
lst.append(num1)
lst.append(num2)

print(max(lst))
