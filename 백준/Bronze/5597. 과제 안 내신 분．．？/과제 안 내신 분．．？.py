import sys

numbers = [number for number in range(1, 31)]

for _ in range(28):
    num = int(sys.stdin.readline())
    numbers.remove(num)

for i in numbers:
    print(i)