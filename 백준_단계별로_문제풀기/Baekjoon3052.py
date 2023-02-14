# https://www.acmicpc.net/problem/3052


# sub = []
# dif = []

# for test_case in range(10):
#     num = int(input())
#     not42 = int(input())%42
#     if not42 != 0:
#         sub.append(not42)
    
#     for i in range(sub+1):
#         if sub[i] != sub[i+1]:
#             dif.append(i)

# print(len(dif))

sub = []
for _ in range(10):
    num = int(input())
    sub.append(num%42)

sub = set(sub)
print(len(sub))