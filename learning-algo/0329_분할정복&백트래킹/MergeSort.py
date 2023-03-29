def merge(left, right):
    pass

def msort(m):
    if len(m) == 1:      # 만약 길이가 1 짜리면 
        return m
    
    middle = len(m)//2      # pythonic
    left = m[0:middle]      # 갈라질 때마다 left, right 생성하므로
    right = m[middle:]      # 메모리 많이 잡아먹음
    # left = []                      # 원래라면
    # right = []
    # middle = len(m)//2
    # for x in range(m[0:middle+1]):
    #     left.append(m[x])
    # for x in range(m[middle:]):
    #     right.append(m[x])

    left = msort(left)
    right = msort(right)
    return merge(left, right)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    msort(arr)