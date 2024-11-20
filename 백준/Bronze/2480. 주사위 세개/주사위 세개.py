import sys
a, b, c = map(int, sys.stdin.readline().split())

l = [a,b,c]
answer = 0
if a == b == c:
    answer += 10000 + a*1000
elif a == b and b != c:
    answer += 1000 + a*100
elif a == c and a != b:
    answer += 1000 + a*100
elif b == c and a != b:
    answer += 1000 + b*100
else:
    answer += max(l)*100
    
print(answer)