N, k = map(int, input().split())
score = list(map(int, input().split()))

score.sort(reverse=True)
cut = score[k-1]

print(cut)