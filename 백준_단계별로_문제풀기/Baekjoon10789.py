word = [input() for _ in range(5)]
mx = 0
for i in range(len(word)):
    if mx < len(word[i]):
        mx = len(word[i])

for i in range(mx):
    for j in range(5):
        if i < len(word[j]):
            print(word[j][i], end = "")


