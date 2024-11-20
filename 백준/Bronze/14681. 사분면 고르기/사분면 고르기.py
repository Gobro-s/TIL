import sys
x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

answer = 0
if x > 0 and y > 0:
    answer += 1
elif x < 0 and y > 0:
    answer += 2
elif x < 0 and y < 0:
    answer += 3
elif x > 0 and y < 0:
    answer += 4

print(answer)