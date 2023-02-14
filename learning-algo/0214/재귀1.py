# 재귀 호출의 기본 구조는 두 개의 인자를 받는다.
# f(i(현재 단계), k(목표))

# f(i, k)             #i: 단계, k: 목표
#     if i == k:      # 목표 도달

#         return
#     else:
#         f(i+1, k)    # 다음 단계

# def f(i, k):
#     if i == k:  # 목표에 도달하면
#         return
#     else:
#         f(i+1, k)



def f(i, k):
    if i == k:
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+k, k)

A = [10,20,30]
B = [0]*3

f(0,3)
