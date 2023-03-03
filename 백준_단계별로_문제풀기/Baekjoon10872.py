# https://www.acmicpc.net/problem/10872

def fact(n):
    nfact = 0
    for i in range(n):
        if i > 1:
            nfact += i*(i-1)
        elif i == 1:
            return 1

fact(10)