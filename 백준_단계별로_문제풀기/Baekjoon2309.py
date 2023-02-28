# https://www.acmicpc.net/problem/2309


num = [int(input()) for _ in range(9)]

for i in range(9):
    for j in range(i +1, 9):
        if sum(num) - (num[i] + num[j]) == 100 and 0 < num[i] <= 100 and 0 < num[j] <= 100:
            num.pop(j)
            num.pop(i)
            break
    if len(num) == 7:
        break

num.sort()
for i in num:
    print(i)


# for i in range(9):
#     temp = sum(num) - num[i]
#     B = num.pop(i)
#     index = i
#     for j in range(8):
#         if temp - num[j] == 100:
#             A = num[j]
#
#             num.remove(A)
#
#             break
#
#     num.insert(index, B)
#
