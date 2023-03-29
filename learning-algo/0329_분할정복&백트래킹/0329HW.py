import sys
sys.stdin = open("0329HW_input.txt", "r")
'''
L[0:N//2] 와 L[N//2:N] 으로 분할  → 원래 분할 정렬
(l[0:N//2])[-1] > L[N//2:N][-1] 횟수
'''


cnt = 0                                           # if left_list[-1] > right_list[-1]:  cnt += 1
def Merge(m):
    global cnt                                    

    if len(m) == 1:                               # 원소가 1개 → 1개를 뭘 정렬을 함ㅋㅋ
        return m
    
    middle = len(m) // 2                          # "분할". left/ right list
    left = Merge(m[0:middle])
    right = Merge(m[middle:])
    # print(left)
    # print(right)
    tmp=[]
    idx = 0                                       # idx : 원래 list의 index
    left_idx = 0                                  # left_idx : left_list's index
    right_idx = 0                                 # right_idx : right_list's index
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            tmp.append(left[left_idx])
            left_idx += 1
            
        else:
            tmp.append(right[right_idx])
            right_idx += 1
        


    if left_idx == len(left):                     # 왼쪽 끝나면
        for i in range(right_idx, len(right)):    # 나머지 다 추가
            m[idx] = right[i]
            idx += 1
    elif right_idx == len(right):                 # 오른쪽 끝나면
                                                  # if left_list[-1] > right_list[-1] : 
                                                  #     left_list에 값이 남음
        cnt += 1                                  # 그럼 그것도 횟수에 추가 해주고
        for i in range(left_idx, len(left)):
            m[idx] = left[i]
            idx += 1
    return m

    
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    L = Merge(nums)                               # 정렬이 끝난 list L
    ans = L[N//2]
    # print(L)
    # print(ans)
    print(f'#{tc} {ans} {cnt}')