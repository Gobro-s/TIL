# https://www.acmicpc.net/problem/9506


while True:
    N = int(input())
    if N == -1:
        break
    lst = []
    for i in range(1, N+1):
        if N % i == 0 and N != i:
            lst.append(i)

    if sum(lst) == N:
        print(N, "=", " + ".join(str(i) for i in lst), sep = " ")

    else:
        print(N, 'is NOT perfect.')