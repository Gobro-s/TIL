import sys
t = sys.stdin.readline().rstrip()
nums = sys.stdin.readline().rstrip()

total = sum(map(int, nums))
print(total)