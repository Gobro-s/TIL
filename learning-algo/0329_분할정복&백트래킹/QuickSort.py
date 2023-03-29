def hoare(A, l, r):
    pivot = A[l]     # 맨 왼쪽 원소를 기준 (꼭 맨 왼쪽이 아니어도 됨)
    i = l            # 피봇보다 큰 값을 찾아 오른쪽으로 이동
    j = r            # 피봇보다 작은 값을 찾아 왼쪽으로 이동
    while i <= j:    # 두 개가 교차하지 않은 상태이면
        while i <= j and A[i] <= pivot:   # 더 큰 애를 만나면 멈추고
            i += 1
        while i <= j and A[j] >= pivot:   # A[j] >= pivot:
            j -= 1
        if i < j:              # 교차하지 않은 경우
            A[i], A[j] == A[j], A[i]
    A[j], A[l] = A[l], A[j]    # 교차해서 while문 탈출한 경우
    return j

def qsort(A, l, r):
    if l < r:
        s = hoare(A, l, r)
        qsort(A, l, s-1)
        qsort(A, s+1, r)


# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    qsort(arr, 0, N-1)
    print(*arr)
    # print(arr[500000])