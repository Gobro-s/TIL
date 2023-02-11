# https://www.acmicpc.net/problem/3003

Whole = [1, 1, 2, 2, 2, 8]
whitenow = list(map(int, input().split()))

for i in range(len(Whole)) :
    Whole[i] -= whitenow[i]
print(*Whole)