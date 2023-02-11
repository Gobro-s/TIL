#https://www.acmicpc.net/problem/2480

a, b, c = map(int, input().split())
abclist = [a, b, c]

if a == b == c:
    print(10000+a*1000)
elif a==b!=c:
    print(1000+a*100)
elif a==c!=b:
    print(1000+a*100)
elif b==c!=a:
    print(1000+b*100)
else:
    print(max(abclist)*100)