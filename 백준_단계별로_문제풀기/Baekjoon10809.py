# https://www.acmicpc.net/problem/10809

S = input()
alpha = list(range(97,123))

for _ in alpha:
    print(S.find(chr(_)))