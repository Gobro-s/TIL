a, b = map(int, input().split())

ayaksoo = []
byaksoo = []
abaesoo = []
bbaesoo = []

for i in range(1, a+1):
    if a % i ==0:
        ayaksoo.append(i)

for i in range(1, b+1):
    if b % i == 0:
        byaksoo.append(i)

gongyaksoo = []
for i in ayaksoo:
    if i in byaksoo:
        gongyaksoo.append(i)

print(max(gongyaksoo))

for i in range(1, b+1):
    abae = i*a
    abaesoo.append(abae)

for i in range(1, a+1):
    bbae = i*b
    bbaesoo.append(bbae)

gongbaesoo = []
for i in abaesoo:
    if i in bbaesoo:
        gongbaesoo.append(i)

print(min(gongbaesoo))
