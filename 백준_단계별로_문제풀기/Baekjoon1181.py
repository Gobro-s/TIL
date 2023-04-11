N = int(input())
words=[]
for _ in range(N):
    words.append(input())
ans = list(set(words))
ans.sort()
ans.sort(key=lambda x: len(x))

# for word in words:
#     if len(words[word]) == 
print(*ans, sep='\n')