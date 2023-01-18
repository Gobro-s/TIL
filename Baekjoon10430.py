#https://www.acmicpc.net/problem/10430

#(A+B)%C == ((A%C) + (B%C))%C  ?
#(A*B)%C == ((A%C)*(B%C))%C  ?

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)