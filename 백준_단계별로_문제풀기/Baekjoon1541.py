nums = input().split('-')

lst = []
for i in nums:
    num = i.split('+')
    sm = 0
    for j in num:
        sm += int(j)
    lst.append(sm)

ans = lst[0]

for j in range(1, len(lst)):
    ans -= lst[(j)]

print(ans)