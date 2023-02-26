# https://www.acmicpc.net/problem/2798


'''
순서
1. 리스트 중에서 세 개 를 뽑고.
2. 세 개를 합쳐본다.
3. 그걸 현재 max값과 비교해서
4. 새로운 합이 더 크고 <=M이면 그것이 max
'''

N, M = map(int, input().split())
num = list(map(int, input().split()))

mx = 0
for i in num:
    for j in num:
        if i != j:
            for k in num:
                if i != k and j != k:
                    if mx < i+j+k and i+j+k <= M:
                        mx = i+j+k
    
print(mx)