# https://www.acmicpc.net/problem/1978

# N = int(input())
# for i in range(N):

#     lst = []
#     cnt = 0
#     num = map(int, input().split())
#     for j in range(num):
#         if num % j == 0:
#             lst.append(j)
#             if len(lst) == 2:
#                 cnt += 1

#     print(cnt)


N= int(input())
num = list(map(int, input().split()))
for i in range(N):
    lst = []
    cnt = 0
    for j in range(N):
        if num % j == 0:
            lst.append(j)
        
            if len(lst) == 2:
                cnt += 1

    print(cnt) 
